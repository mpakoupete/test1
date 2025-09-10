# On part d'une image Python officielle et légère
FROM python:3.9-slim

# On définit le répertoire de travail dans l'image
WORKDIR /app

# On copie d'abord les dépendances pour optimiser le cache de build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie ensuite le reste de notre application
COPY . .

# Commande pour lancer l'application quand le conteneur démarre
CMD ["python", "app.py"]
