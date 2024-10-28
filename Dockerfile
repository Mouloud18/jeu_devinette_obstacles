# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
# COPY . /app
COPY requirements.txt /app

# Installer les dépendances
# RUN pip install flask
RUN pip install -r requirements.txt


# Exposer le port 9090
EXPOSE  9090


# Définir la commande par défaut
CMD ["python", "app.py"]