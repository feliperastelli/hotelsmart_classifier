import pickle
import pandas as pd
import json
import numpy as np
from flask import Flask, request, Response
import os
from hotelsmart.hotelsmart import PredictReservas

model = pickle.load(open('../models/final_model.pkl', 'rb'))

app = Flask(__name__)   

@app.route('/hotelsmart/predict', methods=['POST'])
def emprestimo_predict():
    test_json = request.get_json()

    if test_json:
        if isinstance(test_json, dict):
            test_raw= pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        pipeline = PredictReservas()
        test_cleaned = pipeline.data_cleaning(test_raw)
        test_engineered = pipeline.feature_engineering(test_cleaned)
        test_prepared = pipeline.data_preparation(test_engineered)
        predictions = pipeline.get_predictions(model, test_prepared, test_raw)

        return predictions
    else:
        return Response('{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0', port=port, debug=True)