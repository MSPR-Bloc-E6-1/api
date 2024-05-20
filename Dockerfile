# Utiliser une image de base avec Python 3.11
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 5000

# Définir la commande pour exécuter l'application Flask avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api_IA:app"]
