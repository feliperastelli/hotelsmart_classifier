import pickle
import pandas as pd
import json
import numpy as np

class PredictReservas(object):
    def __init__(self):

        # columns to be used for prediction: ['lead_time', 'market_segment_type', 'avg_price_per_room', 'no_of_special_requests', 'week_of_year']

        self.model = pickle.load(open('models/final_model.pkl', 'rb'))
        self.market_segment_type_encoder = pickle.load(open('.parameters/label_encoder_market_segment_type.pkl', 'rb'))
        self.avg_price_scaler = pickle.load(open('parameters/scaler_avg_price_per_room.pkl', 'rb'))
        self.no_of_special_requests_scaler = pickle.load(open('parameters/scaler_no_of_special_requests.pkl', 'rb'))
        self.week_of_year_scaler = pickle.load(open('parameters/scaler_week_of_year.pkl', 'rb'))

    def data_cleaning(self, df1):

        # Filtra dados para no_of_adults > 0 
        df1 = df1[df1['no_of_adults'] > 0]
        
        return df1
        
    def feature_engineering(self, df2):
        
        df2['total_nights'] = df2['no_of_weekend_nights'] + df2['no_of_week_nights']
        df2['total_guests'] = df2['no_of_adults'] + df2['no_of_children']
        df2['family_trip'] = df2.apply(lambda x: 1 if x['no_of_children'] > 0 else 0, axis=1)

        df2['arrival_date_full'] = pd.to_datetime(
            df2['arrival_year'].astype(str) + '/' +
            df2['arrival_month'].astype(str) + '/' +
            df2['arrival_date'].astype(str),
            errors='coerce'
        )

        df2['day_of_week'] = df2['arrival_date_full'].dt.dayofweek
        df2['week_of_year'] = df2['arrival_date_full'].dt.isocalendar().week 

        numerator = df2['no_of_previous_cancellations']
        denominator = df2['no_of_previous_cancellations'] + df2['no_of_previous_bookings_not_canceled']
        df2['cancellation_ratio_previous'] = numerator / denominator

        df2['cancellation_ratio_previous'].fillna(0, inplace=True)

        return df2
    
    def data_preparation(self, df3):

        # Seleciona colunas para previsão
        df3 = df3[['lead_time', 'market_segment_type', 'avg_price_per_room', 'no_of_special_requests', 'week_of_year']]

        # Rescale
        df3['avg_price_per_room'] = self.avg_price_scaler.transform(df3[['avg_price_per_room']])
        df3['no_of_special_requests'] = self.no_of_special_requests_scaler.transform(df3[['no_of_special_requests']])
        df3['week_of_year'] = self.week_of_year_scaler.transform(df3[['week_of_year']])
        
        # Encode market_segment_type
        df3['market_segment_type'] = self.market_segment_type_encoder.transform(df3['market_segment_type'])

        return df3
    
    def get_predictions(self, model, test_data, original_data):

        pred = model.predict(test_data)
        original_data['prediction'] = pred

        return original_data.to_json(orient='records')
