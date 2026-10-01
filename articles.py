"""Articles du site. Ajoutez vos propres articles ici."""


def charger_articles():
    return [
        {
            "slug": "ia-generative-creation-contenu",
            "titre": "L'IA générative transforme la création de contenu",
            "categorie": "Tech",
            "date": "2026-09-28",
            "resume": (
                "Les outils d'intelligence artificielle permettent désormais de rédiger, "
                "illustrer et structurer des idées en quelques secondes. Tour d'horizon "
                "des usages concrets pour les créateurs indépendants."
            ),
            "paragraphes": [
                "Rédaction d'articles, génération de visuels, idées de vidéos : les modèles de langage sont devenus des assistants du quotidien. Là où il fallait des heures pour structurer un article, quelques minutes suffisent désormais pour obtenir une première version exploitable.",
                "L'essentiel reste d'apporter sa touche personnelle : l'outil propose, le créateur dispose. Les contenus les plus appréciés — par les lecteurs comme par les moteurs de recherche — sont ceux qui combinent la rapidité de la machine et l'expérience humaine.",
                "Concrètement, les créateurs utilisent l'IA pour trois tâches principales : le brainstorming (générer 20 angles d'attaque pour un sujet), la structuration (transformer des notes en plan clair) et la reformulation (adapter un texte à un autre public).",
                "Attention toutefois : publier du contenu 100 % généré sans relecture est sanctionné par Google. La valeur ajoutée humaine — anecdotes, opinions, vérification des faits — reste indispensable pour un contenu de qualité.",
            ],
        },
        {
            "slug": "apprendre-a-coder-efficacement",
            "titre": "5 habitudes pour apprendre à coder efficacement",
            "categorie": "Apprentissage",
            "date": "2026-09-25",
            "resume": (
                "Coder tous les jours un peu vaut mieux que beaucoup une fois par mois. "
                "Voici les habitudes qui font vraiment progresser."
            ),
            "paragraphes": [
                "1. Construire des petits projets finis plutôt que de suivre des tutoriels sans fin. Un projet terminé, même modeste, enseigne plus que dix heures de vidéo : il confronte aux vrais problèmes — bugs, organisation du code, choix techniques.",
                "2. Lire le code des autres. GitHub regorge de projets open source bien écrits. Comprendre comment un développeur expérimenté structure son travail est une formation en soi.",
                "3. Documenter ce que l'on apprend. Tenir un carnet de notes, même succinct, transforme une découverte passagère en connaissance durable.",
                "4. Accepter de bloquer. Rester coincé fait partie du métier : c'est en cherchant — documentation, forums, essais — que l'on retient vraiment.",
                "5. Partager ses créations, même imparfaites. Les retours d'autres développeurs sont le meilleur professeur, et un portfolio public ouvre des portes professionnelles.",
            ],
        },
        {
            "slug": "monetiser-site-web-bases",
            "titre": "Monétiser un site web : les bases à connaître",
            "categorie": "Business",
            "date": "2026-09-20",
            "resume": (
                "Publicité display, affiliation, contenus sponsorisés : panorama des "
                "modèles de revenus accessibles aux petits éditeurs."
            ),
            "paragraphes": [
                "La publicité display (AdSense et ses alternatives) rémunère à l'affichage ou au clic. C'est le modèle le plus simple à mettre en place : quelques lignes de code suffisent une fois le site approuvé.",
                "L'affiliation rapporte une commission sur les ventes générées par vos liens. Amazon Partenaires, programmes logiciels, formations en ligne : les taux varient de 1 % à 50 % selon les produits.",
                "Les contenus sponsorisés — articles rémunérés par une marque — demandent une audience déjà établie, mais rapportent bien plus par article que la publicité classique.",
                "Dans tous les cas, la règle d'or reste identique : du contenu utile et original, publié régulièrement. Sans trafic, pas de revenus ; sans qualité, pas de trafic.",
            ],
        },
        {
            "slug": "heberger-site-gratuitement",
            "titre": "Héberger son site gratuitement : les options en 2026",
            "categorie": "Tech",
            "date": "2026-09-15",
            "resume": (
                "Render, PythonAnywhere, GitHub Pages : où héberger un site sans payer "
                "un centime quand on débute ?"
            ),
            "paragraphes": [
                "Pour un site statique (HTML/CSS/JS), GitHub Pages et Netlify offrent un hébergement gratuit illimité avec HTTPS inclus. C'est la solution idéale pour un blog ou un portfolio.",
                "Pour un site dynamique en Python (Flask, Django), Render et PythonAnywhere proposent des offres gratuites suffisantes pour débuter. Limite : le site se met en veille après une période d'inactivité et met quelques secondes à redémarrer.",
                "Le passage à un hébergement payant (3 à 6 €/mois chez o2switch, Hostinger ou OVH) ne devient nécessaire que lorsque le trafic dépasse quelques milliers de visiteurs par mois.",
                "Notre conseil : commencez gratuit, validez votre concept et votre trafic, puis investissez uniquement quand les revenus publicitaires couvrent les frais.",
            ],
        },
        {
            "slug": "seo-debutant-guide",
            "titre": "SEO : le guide du débutant pour être visible sur Google",
            "categorie": "Business",
            "date": "2026-09-10",
            "resume": (
                "Être premier sur Google ne s'achète pas, ça se mérite. Les fondations "
                "techniques et éditoriales à poser dès le premier jour."
            ),
            "paragraphes": [
                "Le SEO (référencement naturel) repose sur trois piliers : la technique, le contenu et la popularité. Négliger l'un des trois compromet tout l'édifice.",
                "Côté technique : un site rapide, adapté au mobile, avec des balises titre et description soignées, un sitemap.xml et un robots.txt propres. Ces fondations sont simples à mettre en place et font toute la différence.",
                "Côté contenu : chaque page doit répondre à une question précise que se posent vos lecteurs. Les outils gratuits comme Google Search Console révèlent les requêtes qui vous amènent déjà du trafic.",
                "Côté popularité : les liens d'autres sites vers le vôtre restent le signal de confiance le plus fort. Ils s'obtiennent naturellement avec du contenu remarquable, des partenariats et du temps.",
            ],
        },
        {
            "slug": "creer-premiere-application-python",
            "titre": "Créer sa première application Python de A à Z",
            "categorie": "Apprentissage",
            "date": "2026-09-05",
            "resume": (
                "De l'idée au logiciel fonctionnel : les étapes concrètes pour transformer "
                "un concept en application utilisable."
            ),
            "paragraphes": [
                "Tout commence par une idée précise : quel problème votre application résout-elle ? Écrivez-le en une phrase. Si vous n'y arrivez pas, l'idée n'est pas encore assez mûre.",
                "Ensuite, dessinez l'interface sur papier avant d'écrire la moindre ligne de code. Cette étape simple évite des heures de refactoring.",
                "Choisissez ensuite votre boîte à outils : Tkinter ou CustomTkinter pour une application desktop, Flask pour un site web, Kivy pour le mobile. Python couvre tous les terrains.",
                "Développez par petites versions : une V0.1 qui fait une seule chose, puis des améliorations successives. C'est la méthode qui mène réellement à un produit fini.",
            ],
        },
    ]
