# Utiliser l'image officielle Python 3.10 comme image de base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer Poetry
RUN pip install poetry

# Copier les fichiers de configuration de Poetry dans le conteneur
COPY pyproject.toml poetry.lock* /app/

# Configurer Poetry pour ne pas créer de virtual envs à l'intérieur du conteneur
RUN poetry config virtualenvs.create false

# Installer les dépendances en utilisant Poetry
RUN poetry install --no-dev

# Copier le reste des fichiers du projet dans le conteneur
COPY . /app

# Exposer le port sur lequel FastAPI va s'exécuter
EXPOSE 8000

# Commande pour exécuter l'application FastAPI avec uvicorn
CMD ["uvicorn", "generation_service.main:app", "--host", "0.0.0.0", "--port", "8001"]
