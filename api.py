import subprocess
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

def installer_dependances(fichier_requirements):
    """Installe les dépendances du fichier requirements.txt."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", fichier_requirements])

def lancer_script(script):
    """Lance un script Python."""
    subprocess.Popen([sys.executable, script])

if __name__ == "__main__":
    # Chemin vers le fichier requirements.txt
    fichier_requirements = "requirements.txt"
    
    # Installer les dépendances
    print("Installation des dépendances...")
    installer_dependances(fichier_requirements)
    
    # Lancer les scripts Python
    print("Lancement de api_BDD.py...")
    lancer_script("api_BDD.py")
    print("Lancement de api_IA.py...")
    lancer_script("api_IA.py")
