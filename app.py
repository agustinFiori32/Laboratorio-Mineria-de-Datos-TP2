from flask import Flask, request, jsonify
import pickle
import numpy as np

model_path = 'src/random_forest_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return "API para Clasificación de Clientes con Random Forest."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)

        
        prediction = model.predict(features)[0]

        return jsonify({
            'prediction': prediction
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
