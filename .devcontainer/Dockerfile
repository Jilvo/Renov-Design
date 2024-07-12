# Utiliser une image Python officielle
FROM python:3.10-slim

# Créer un utilisateur non-root pour VS Code
RUN useradd -ms /bin/bash vscode

# Installer les dépendances du système
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Définir l'utilisateur vscode
USER vscode

# Définir le répertoire de travail
WORKDIR /workspace

# Copier les fichiers de requirements.txt s'ils existent
COPY requirements.txt /workspace/requirements.txt

# Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exposer le port 8000 (optionnel, si vous avez une application web)
EXPOSE 8000

# Définir l'entrée par défaut du conteneur
CMD ["python"]
