"""
MonSite — Site complet prêt pour Google AdSense.
Local    : C:/Documents/.venv/Scripts/python.exe app.py
Production : gunicorn app:app (géré automatiquement par Render)
"""
import os
from flask import Flask, render_template, abort, url_for, Response
from articles import charger_articles

app = Flask(__name__)

# ============================================================
# CONFIGURATION — À PERSONNALISER AVANT MISE EN LIGNE
# ============================================================
NOM_SITE = "MonSite"
# En local : http://127.0.0.1:5000 — en ligne, Render remplit RENDER_EXTERNAL_URL automatiquement.
URL_SITE = os.environ.get("RENDER_EXTERNAL_URL", "http://127.0.0.1:5000")
EMAIL_CONTACT = "contact@monsite.com"  # Votre vraie adresse

# ============================================================
# ADSENSE
# 1. Inscription : https://adsense.google.com
# 2. Après approbation, collez votre ID éditeur ci-dessous.
# Tant qu'il est vide, le site affiche des emplacements
# factices (mode démo) sans violer le règlement AdSense.
# ============================================================
ADSENSE_CLIENT = "ca-pub-3123168388364435"
ADSENSE_SLOT_BANNIERE = "1111111111"
ADSENSE_SLOT_CONTENU = "2222222222"
ADSENSE_SLOT_LATERAL = "3333333333"


def contexte_commun():
    """Variables transmises à tous les templates."""
    return {
        "nom_site": NOM_SITE,
        "url_site": URL_SITE,
        "adsense_client": ADSENSE_CLIENT,
        "slot_banniere": ADSENSE_SLOT_BANNIERE,
        "slot_contenu": ADSENSE_SLOT_CONTENU,
        "slot_lateral": ADSENSE_SLOT_LATERAL,
    }


# ---------------- Pages principales ----------------

@app.route("/")
def accueil():
    articles = charger_articles()
    return render_template(
        "index.html",
        articles=articles[:3],
        titre_page=f"{NOM_SITE} — Actus Tech & IA",
        description_page="Articles sur la tech, l'IA, le code et la monétisation en ligne.",
        **contexte_commun(),
    )


@app.route("/articles")
def liste_articles():
    articles = charger_articles()
    return render_template(
        "liste_articles.html",
        articles=articles,
        titre_page=f"Tous les articles — {NOM_SITE}",
        description_page="Retrouvez tous nos articles tech, apprentissage et business.",
        **contexte_commun(),
    )


@app.route("/article/<slug>")
def article(slug):
    articles = {a["slug"]: a for a in charger_articles()}
    if slug not in articles:
        abort(404)
    return render_template(
        "article.html",
        article=articles[slug],
        titre_page=f"{articles[slug]['titre']} — {NOM_SITE}",
        description_page=articles[slug]["resume"],
        **contexte_commun(),
    )


# ---------------- Pages obligatoires pour AdSense ----------------

@app.route("/a-propos")
def a_propos():
    return render_template(
        "page.html",
        titre_page=f"À propos — {NOM_SITE}",
        description_page=f"Qui sommes-nous ? Découvrez {NOM_SITE}.",
        titre_contenu="À propos",
        paragraphes=[
            f"{NOM_SITE} est un média indépendant dédié à la tech, à l'intelligence "
            "artificielle, à l'apprentissage du code et à la monétisation en ligne.",
            "Notre mission : rendre accessible des sujets techniques grâce à des "
            "articles clairs, pratiques et régulièrement mis à jour.",
            "Le site est financé par la publicité display (Google AdSense), ce qui "
            "nous permet de proposer l'intégralité du contenu gratuitement.",
            "Pour toute question ou proposition, utilisez la page Contact.",
        ],
        **contexte_commun(),
    )


@app.route("/contact")
def contact():
    return render_template(
        "page.html",
        titre_page=f"Contact — {NOM_SITE}",
        description_page="Contactez-nous.",
        titre_contenu="Contact",
        paragraphes=[
            "Une question, une suggestion de sujet, un partenariat ?",
            f"Écrivez-nous à : {EMAIL_CONTACT}",
            "Nous répondons généralement sous 48 heures ouvrées.",
        ],
        **contexte_commun(),
    )


@app.route("/politique-de-confidentialite")
def confidentialite():
    return render_template(
        "page.html",
        titre_page=f"Politique de confidentialité — {NOM_SITE}",
        description_page="Politique de confidentialité et gestion des cookies.",
        titre_contenu="Politique de confidentialité",
        paragraphes=[
            "Cette page décrit la manière dont ce site traite les informations "
            "relatives à ses visiteurs.",
            "Cookies publicitaires : ce site utilise Google AdSense pour afficher "
            "des annonces. Google et ses partenaires peuvent déposer des cookies "
            "afin de diffuser des publicités personnalisées en fonction de vos "
            "visites sur ce site et d'autres sites.",
            "Vous pouvez désactiver la publicité personnalisée à tout moment via "
            "les Paramètres des annonces Google : https://adssettings.google.com",
            "Données collectées : ce site ne collecte aucune donnée personnelle "
            "via des formulaires. Les seules données techniques sont celles "
            "collectées automatiquement par les services publicitaires tiers.",
            f"Contact : {EMAIL_CONTACT}",
        ],
        **contexte_commun(),
    )


# ---------------- Fichiers SEO obligatoires ----------------

@app.route("/ads.txt")
def ads_txt():
    """Fichier ads.txt exigé par AdSense pour vérifier le site."""
    contenu = f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n"
    return Response(contenu, mimetype="text/plain")


@app.route("/robots.txt")
def robots():
    contenu = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {URL_SITE}/sitemap.xml\n"
    )
    return Response(contenu, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    pages = [
        url_for("accueil", _external=True),
        url_for("liste_articles", _external=True),
        url_for("a_propos", _external=True),
        url_for("contact", _external=True),
        url_for("confidentialite", _external=True),
    ]
    for article in charger_articles():
        pages.append(url_for("article", slug=article["slug"], _external=True))

    urls = "".join(f"  <url><loc>{p}</loc></url>\n" for p in pages)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}"
        "</urlset>"
    )
    return Response(xml, mimetype="application/xml")


# ---------------- Erreurs ----------------

@app.errorhandler(404)
def page_introuvable(e):
    return render_template(
        "page.html",
        titre_page=f"Page introuvable — {NOM_SITE}",
        description_page="Cette page n'existe pas.",
        titre_contenu="404 — Page introuvable",
        paragraphes=["Le contenu demandé n'existe pas ou a été déplacé."],
        **contexte_commun(),
    ), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("RENDER") is None  # debug uniquement en local
    app.run(debug=debug, host="0.0.0.0", port=port)
