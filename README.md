# Installation / Utilisation:

Pour installer et utiliser l'api vous devez lancer le fichier `api.py`:
> python api.py

&nbsp; 
# API:
## IA:
L'accès à l'IA est possible sur l'endpoint `$url/predict` avec la méthode `POST`. Une seule image doit être fournie dans la requête.  
La réponse de l'api sera un string contenant le nom de l'animal:
```
Animal
```
### Fonctionnement:
Tout d'abord, l'API vérifie la conformité de la requête en s'assurant qu'elle contient un fichier, qu'il n'y a pas plus d'un fichier fourni, et que le fichier fourni est effectivement une image.  

Ensuite, un fichier temporaire correspondant à l'image fournie est créé pour permettre le traitement ultérieur.  

L'image temporaire est ensuite préparée pour le traitement par l'IA. Cela inclut le redimensionnement de l'image en 128x128 pixels et sa conversion en un tableau numpy.  

Une fois l'image prétraitée, elle est soumise au modèle d'IA. Le modèle renvoie une prédiction sous forme d'un vecteur de probabilités où chaque élément correspond à la probabilité que l'image appartienne à une classe spécifique d'animal.  

La classe prédite est déterminée en sélectionnant l'indice ayant la probabilité la plus élevée dans le vecteur de prédiction. Ce numéro de classe est ensuite converti en nom d'animal en utilisant un dictionnaire préalablement défini.  

Après avoir obtenu le nom de l'animal prédit, le fichier temporaire est supprimé et le nom de l'animal est renvoyé en réponse à la requête.  


## Infos Animaux:
L'accès aux information des animaux est possible sur l'endpoint `$url/api/explication/animals` avec la méthode `GET`. Il est nécessaire de passer le nom de l'animal en paramètre.  
la réponse de l'api sera un json sous ce format:
```
[
    {
        "description": "description de l'animal (string)",
        "famille": "famille de l'animal (string)",
        "habitat": "habitat de l'animal (string)",
        "imageAnimal": "photo de l'animal au format base64 (string)",
        "nom": "nom de l'animal (string)",
        "numAnimal": id de l'animal (int),
        "taille": "taille de l'animal (string)"
    }
]
```
### Fonctionnement:
Tout d'abord, l'API assure la conformité de la requête en vérifiant la présence d'un paramètre 'name'. Si ce paramètre n'est pas inclus dans la requête, un message d'erreur est renvoyé avec un code de statut 400.  

Ensuite, la connexion à la base de données est établie en utilisant les informations de connexion prédéfinies (hôte, nom d'utilisateur, mot de passe, nom de la base de données). Si la connexion échoue, un message d'erreur est renvoyé avec un code de statut 500.  

Une fois la connexion à la base de données réussie, une requête SQL est exécutée pour sélectionner les informations sur l'animal spécifié par le paramètre 'name'. Si aucun animal correspondant n'est trouvé dans la base de données, un message d'erreur est renvoyé avec un code de statut 404.  

Si des informations sur l'animal sont trouvées, elles sont récupérées à partir du résultat de la requête SQL. L'image de l'animal, stockée sous forme de BLOB dans la base de données, est convertie en base64 pour pouvoir être incluse dans la réponse JSON.  

Les informations sur l'animal, y compris l'image convertie en base64, sont rassemblées dans un dictionnaire pour chaque animal trouvé. Ces dictionnaires sont ensuite ajoutés à une liste d'animaux.  

Enfin, la liste d'animaux est renvoyée en réponse à la requête, avec un code de statut 200 pour indiquer que la requête a réussi.  

Si une erreur survient à tout moment du processus, un message d'erreur approprié est renvoyé avec le code de statut correspondant pour informer le client de l'erreur rencontrée.  

&nbsp; 
&nbsp; 
# Docker
## Installation et Configuration:
Pour installer et configurer les différents services nécessaires à l'API, nous utilisons Docker et Docker Compose.  

### Fichier docker-compose.yml:  
Le fichier `docker-compose.yml` définit plusieurs services: MySQL pour la base de données, phpMyAdmin pour la gestion de la base de données, et deux services API distincts pour la reconnaissance d'images et les informations sur les animaux.

### Dockerfile.api_bdd:
Le Dockerfile `Dockerfile.api_bdd` est utilisé pour créer l'image du service `api_bdd`. Il configure l'environnement Python, copie les fichiers nécessaires, installe les dépendances, et expose le port 3001.

### Dockerfile.api_IA:
Le Dockerfile `Dockerfile.api_IA` est utilisé pour créer l'image du service `api_IA`. Il configure également l'environnement Python, copie les fichiers nécessaires, installe les dépendances, et expose le port 5000.


## Fonctionnement:
### Lancement des Services:
Pour démarrer les services définis dans `docker-compose.yml`, utilisez la commande suivante dans le répertoire contenant le fichier docker-compose.yml:  
```
docker-compose up
```
Cette commande téléchargera les images nécessaires, construira les images locales, et démarrera les conteneurs pour chaque service.

### Accès aux Services:
- Base de Données MySQL: Accessible sur le port 3306.
- phpMyAdmin: Accessible sur le port 8080 via l'URL http://localhost:8080.
- API IA: Accessible sur le port 5000 via l'URL http://localhost:5000.
- API BDD: Accessible sur le port 3001 via l'URL http://localhost:3001.  

### Arrêt des Services:
Pour arrêter et supprimer les conteneurs, les réseaux, et les volumes définis dans docker-compose.yml, utilisez la commande suivante:
```
docker-compose down
```
### Rebuild des Images:
Si vous apportez des modifications aux Dockerfiles ou aux dépendances, vous pouvez reconstruire les images avec la commande:
```
docker-compose build
```