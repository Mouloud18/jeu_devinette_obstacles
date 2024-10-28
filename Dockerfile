# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /jeu_devinette_obstacles

# Copier les fichiers du projet dans le conteneur
COPY . /jeu_devinette_obstacles
COPY requirements.txt /jeu_devinette_obstacles

# Installer les dépendances
# RUN pip install flask
RUN pip install --upgrade pip -r requirements.txt


# Exposer le port 5001
EXPOSE  5002


# Définir la commande par défaut
CMD ["python", "jeu_devinette_obstacles.py"]