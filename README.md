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

## Ports

- 8000 : Stockage-service
- 8001 : Generation-service
