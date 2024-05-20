from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tempfile
import os

app = Flask(__name__)
CORS(app)

# Mise à jour des chemins pour les fichiers du modèle
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_FOLDER, 'overfit.h5')
model = load_model(MODEL_PATH)

def prepare_image(img_path, target_size=(224, 224)):  # Mise à jour de la taille cible
    img = load_img(img_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier fourni.'}), 418

    if len(request.files.getlist('file')) > 1:
        return jsonify({'error': 'Trop de fichiers fournis.'}), 400
    
    if request.files['file'].content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
        return jsonify({'error': 'Le fichier doit être une image.'}), 400
    
    file = request.files['file']
    # Créer un fichier temporaire pour l'image uploadée
    temp_dir = tempfile.gettempdir()
    temp_file = tempfile.NamedTemporaryFile(delete=False, dir=temp_dir, suffix='.jpg')
    file_path = temp_file.name
    file.save(file_path)
    temp_file.close()  # S'assurer que le fichier est fermé
    
    image = prepare_image(file_path)
    prediction = model.predict(image) 
    class_index = np.argmax(prediction)
    classes = {0: 'background', 1: 'Ours', 2: 'Castor', 3: 'Chat', 4: 'Coyote', 5: 'Chien', 6: 'Renard', 7: 'Lynx', 8: 'Puma', 9: 'Lapin', 10: 'Raton-laveur', 11: 'Rat', 12: 'Ecureuil', 13: 'Loup'}
    predicted_class = classes[class_index]
    
    # Supprimer le fichier temporaire
    os.remove(file_path)  # Maintenant, cela devrait fonctionner sans erreur
    
    return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    app.run(debug=False)
