# Utilisez une image de base Python
FROM python:3.11.4

# Définissez un répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre projet dans le conteneur
COPY . /app

# Installez les dépendances de votre projet
RUN pip install -r requirements.txt

# Exposez le port que votre application Flask utilise (par défaut, c'est 5000)
EXPOSE 5000

# Définissez une variable d'environnement pour Flask
ENV FLASK_APP=app.py

# Indiquez à Flask de fonctionner en mode de développement (facultatif)
ENV FLASK_ENV=development

# Commande pour démarrer votre application Flask
CMD ["flask", "run", "--host=0.0.0.0"]
