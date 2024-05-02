import subprocess

def lancer_apis():
    # Chemin vers votre interpréteur Python; ajustez selon votre environnement.
    python_executable = "python" 
    
    # Liste des commandes à exécuter
    commandes = [
        [python_executable, "api_predict.py"],
        [python_executable, "api_bdd.py"]
    ]
    
    # Liste pour stocker les processus
    processus = []
    
    for commande in commandes:
        # Lancement de chaque fichier API dans son propre processus
        p = subprocess.Popen(commande)
        processus.append(p)
    
    # Attendre que tous les processus soient terminés
    for p in processus:
        p.wait()

if __name__ == "__main__":
    lancer_apis()
