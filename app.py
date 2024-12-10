from flask import Flask, request, jsonify
import numpy as np
import joblib
import pandas as pd

# Cargar el modelo
model_path = 'src/random_forest_model.pkl'

with open(model_path, 'rb') as f:
    model = joblib.load(model_path) 

print(type(model))

app = Flask(__name__)

@app.route('/')
def home():
    return "API para Clasificación de Clientes con Random Forest."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        features = pd.DataFrame([data['features']])

        features = pd.get_dummies(features)

        model_columns = model.feature_importances_

        features = features.reindex(columns=model_columns, fill_value=0)
        
        if model is None:
            return jsonify({'error': 'Modelo no cargado'}), 500

        prediction = model.predict(features)[0]

        return jsonify({
            'prediction': prediction
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Ejecutar la aplicación solo si el script es ejecutado directamente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

