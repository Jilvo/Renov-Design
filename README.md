# Renov-Design

## Description
L'application Nom de l'Application est une plateforme de transformation d'image basée sur l'IA, permettant aux utilisateurs de modifier le style de décoration d'intérieur de leurs images. Elle est construite en utilisant une architecture de microservices pour une meilleure modularité et évolutivité.

##  Architecture des Microservices
   L'application est composée des microservices suivants :

- **User Service** : Gère l'authentification des utilisateurs (Flask).
- **Payment Service** : Gère les paiements et les abonnements (Django, PayPal, Stripe).
- **Storage Service** : Gère le stockage et la récupération des images (FastAPI).
- **Gateway Service** : Sert de point d'entrée unique pour les requêtes (Kong).
- **Generation Service** : Transforme les images en appliquant différents styles de décoration (FastAPI).
- **Frontend Service** : Interface utilisateur pour interagir avec les différents services (React/Vue/Angular).

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.10+ : [Installation Python](https://www.python.org/downloads/)
- Docker et Docker Compose : [Installation Docker](https://docs.docker.com/engine/install/)
- just : [Repo Github de Just](https://github.com/casey/just)
- pre-commit : [Installation pre-commit](https://pre-commit.com/)
- npm : [Installation npm](https://docs.npmjs.com/cli/v10/commands/npm-install)
- vue.js [Installation vue.js](https://vuejs.org/guide/quick-start)
## Ports

- 8081 : Stockage-service
- 9000 (8000) : Generation-service
- 5000 : User-service
- 5173 : Front-service Vue.js
- 

## Documentation
Created with Sphinx and Readthedocs
https://renov-design.readthedocs.io/en/latest/
### Update the Documentation 
``` 
python generate_docs.py 
```
ls -l stockage_service/docs
ls -l stockage_service/infrastructure

in /docs
```
make clean
make html
```

    list_prompt = [
        "Transform the image to reflect a clean, streamlined design with handle-less cabinets, smooth surfaces, and a neutral color palette featuring whites, grays, and black accents.",
        "Modify the image to include rustic elements like raw wood cabinetry, open shelving, and accessories in wrought iron or copper.",
        "Adapt the image with features typical of Scandinavian design, such as light wood tones, simple lines, and functionality, accented with pastel colors.",
        "Rework the image to showcase industrial elements like exposed piping, metal light fixtures, and a use of materials like stainless steel and concrete for a robust feel.",
        "Alter the image to embody a traditional aesthetic with ornate woodwork, classic details, and rich color schemes, often incorporating patterns like plaids or florals.",
        "Update the image to exhibit Art Deco flair with geometric patterns, bold streamlined forms, and luxurious materials like marble and gold.",
        "Revise the image to blend contemporary design with eclectic accessories, featuring a mix of modern lines and varied textures or global décor influences.",
        "Enhance the image to depict a high-tech kitchen with the latest appliances, smart home technology, and a sleek, modern look that incorporates glossy surfaces and high-end materials.",
        "Transform the kitchen image to a bohemian style with vibrant colors, mixed patterns, and a collection of eclectic, artisanal, and vintage decor.",
        "Modify the image to present a farmhouse style with apron sinks, open shelving, and a mix of rustic and modern elements that create a cozy, welcoming space.",
    ]
    docker run -d -p 8081:8000 stockage_service


## Test SDXL
A chaque fois il y aura 3 prompt différents
`folder name : test_1 pour tester num_inference_steps`

`folder name : test_2 pour tester guidance_scale`

num_inference_steps
Description : Ce paramètre spécifie le nombre d'étapes d'inférence que le modèle de diffusion doit effectuer pour générer une image.
Impact :
Qualité de l'image : Un nombre plus élevé d'étapes d'inférence peut améliorer la qualité de l'image générée, car le modèle a plus d'opportunités pour affiner les détails de l'image.
Temps de calcul : Plus le nombre d'étapes est élevé, plus le temps de calcul sera long. Il y a donc un compromis entre la qualité de l'image et le temps nécessaire pour la générer.
Exemple : num_inference_steps=50 signifie que le modèle effectuera 50 étapes d'inférence pour générer l'image.
guidance_scale
Description : Ce paramètre contrôle l'intensité de la guidance du modèle vers le prompt fourni. Il ajuste l'équilibre entre la fidélité au prompt et la diversité des images générées.
Impact :
Fidélité au prompt : Une valeur plus élevée de guidance_scale rendra l'image générée plus conforme au prompt. Cela signifie que le modèle suivra de plus près les instructions données dans le prompt.
Diversité des images : Une valeur plus faible de guidance_scale permet plus de diversité et de créativité dans les images générées, mais elles peuvent être moins fidèles au prompt.
Exemple : guidance_scale=7.5 signifie que le modèle suivra fortement le prompt, tandis qu'une valeur de guidance_scale=0.0 permettrait au modèle de générer des images plus variées et moins contraintes par le prompt.