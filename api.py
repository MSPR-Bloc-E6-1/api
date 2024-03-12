from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tempfile
import os

app = Flask(__name__)

MODEL_PATH = './model.h5'
model = load_model(MODEL_PATH)

def prepare_image(img_path, target_size=(128, 128)):
    img = load_img(img_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier fourni.'}), 400

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
    classes = {0: 'background', 1: 'beaver', 2: 'cat', 3: 'dog', 4: 'coyote', 5: 'squirrel', 6: 'rabbit', 7: 'wolf', 8: 'lynx', 9: 'bear', 10: 'puma', 11: 'rat', 12: 'raccoon', 13: 'fox'}
    predicted_class = classes[class_index]
    
    # Supprimer le fichier temporaire
    os.remove(file_path)  # Maintenant, cela devrait fonctionner sans erreur
    
    return jsonify({predicted_class})


if __name__ == '__main__':
    app.run(debug=True)