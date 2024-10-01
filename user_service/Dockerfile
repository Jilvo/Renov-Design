# Utiliser une image Python officielle
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers `pyproject.toml` et `poetry.lock` pour installer les dépendances
COPY pyproject.toml poetry.lock /app/

# Installer Poetry
RUN pip install poetry

# Installer les dépendances du projet (sans créer un environnement virtuel)
RUN poetry install --no-root 

RUN poetry add piccolo

# Copier tout le contenu du projet dans le conteneur
COPY . /app


RUN chmod +x /app/install.sh
# Exposer le port sur lequel l'application sera disponible
EXPOSE 5000

# Démarrer l'application avec uvicorn
CMD ["/bin/sh", "-c", "/app/install.sh && poetry run uvicorn run:asgi_app --host 0.0.0.0 --port 5000"]