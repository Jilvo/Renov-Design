# Utiliser une image Python officielle
FROM python:3.12-slim

# Créer un utilisateur non-root pour VS Code
RUN useradd -ms /bin/bash vscode

# Installer les dépendances du système
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /workspace

# Copier les fichiers de requirements.txt s'ils existent avec le bon propriétaire
COPY --chown=vscode:vscode . /workspace

# Installer les dépendances Python
RUN pip install --upgrade pip
# Installer les dépendances Python avec Poetry
RUN python -m venv /workspace/venv
RUN curl -sSL https://install.python-poetry.org | python3 -

# Changer le propriétaire du répertoire de travail au nouvel utilisateur
RUN chown -R vscode:vscode /workspace

# Définir l'utilisateur vscode
USER vscode

# Exposer le port 8000 (optionnel, si vous avez une application web)
EXPOSE 8000

# Définir l'entrée par défaut du conteneur
CMD ["python"]
