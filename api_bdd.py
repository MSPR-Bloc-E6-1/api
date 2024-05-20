from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import base64

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user="root",
            password="rootpassword",
            database="wildlens"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"L'erreur '{e}' est survenue")
        return None

@app.route('/api/explication/animals', methods=['GET'])
def get_animal():
    nom = request.args.get('name')
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        select_query = """
        SELECT numAnimal, imageAnimal, nom, description, famille, taille, habitat 
        FROM animal 
        WHERE nom = %s
        """
        cursor.execute(select_query, (nom,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        
        if len(result) == 0:
            return jsonify({"message": "Aucun animal trouvé"}), 404
        
        animals = []
        for row in result:
            numAnimal, image_blob, nom, description, famille, taille, habitat = row
            # Convertir le BLOB en base64
            image_base64 = base64.b64encode(image_blob).decode('utf-8') if image_blob else None
            
            animal_dict = {
                "numAnimal": numAnimal,
                "imageAnimal": image_base64,
                "nom": nom,
                "description": description,
                "famille": famille,
                "taille": taille,
                "habitat": habitat
            }
            
            animals.append(animal_dict)
        
        return jsonify(animals), 200
    else:
        return jsonify({"message": "Erreur lors de la connexion à la base de données"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=False)

