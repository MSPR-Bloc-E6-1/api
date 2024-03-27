# Installation:

Pour installer vous devez lancer la commande:
> pip install -r requirements.txt

# API

## IA
L'accès à l'IA est possible sur l'endpoint `$url/predict` avec la méthode `POST`. Une et une seule image doit être fournie dans la requête.  
La réponse de l'api sera un string contenant le nom de l'animal.

## Infos Animaux
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