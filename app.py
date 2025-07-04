import pickle
import pandas as pd
import json
import numpy as np
from flask import Flask, request, jsonify
import os
from hotelsmart.hotelsmart import PredictReservas

# Carrega o modelo uma única vez
model = pickle.load(open('models/final_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/hotelsmart/predict', methods=['POST'])
def predict_reservas():
    try:
        test_json = request.get_json(force=True)
        print("🔹 Payload recebido:", test_json)

        if not test_json:
            return jsonify({"error": "JSON vazio ou inválido."}), 400

        # Transforma em DataFrame
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame([test_json])
        else:
            test_raw = pd.DataFrame(test_json)

        print("🔹 DataFrame recebido:\n", test_raw.head())

        pipeline = PredictReservas()

        test_cleaned = pipeline.data_cleaning(test_raw)
        print("🔹 Após limpeza:", test_cleaned.shape)

        test_engineered = pipeline.feature_engineering(test_cleaned)
        print("🔹 Após feature engineering:", test_engineered.shape)

        test_prepared = pipeline.data_preparation(test_engineered)
        print("🔹 Após data preparation:", test_prepared.shape)

        predictions = pipeline.get_predictions(model, test_prepared, test_raw)
        print("✅ Previsão realizada com sucesso.")

        return predictions, 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
