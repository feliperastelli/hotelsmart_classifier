import streamlit as st
import requests
import pandas as pd
import json


def predict(data):
    url = 'https://political-squid-feliperastelli-97cad387.koyeb.app/hotelsmart/predict'
    header = {'Content-Type': 'application/json'}
    data = json.dumps(data.to_dict('records'))
    r = requests.post(url, data=data, headers=header)
    prediction = r.json()[0]['prediction']

    return prediction
# 
st.set_page_config(
    layout="wide",
    page_title="Previsão de Cancelamento de Reservas",
    page_icon="📊"
)

st.title("Previsão de Cancelamento de Reservas")


# ['no_of_adults', 'no_of_children', 'no_of_weekend_nights',
#        'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space',
#        'room_type_reserved', 'lead_time', 'arrival_year', 'arrival_month',
#        'arrival_date', 'market_segment_type', 'repeated_guest',
#        'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled',
#        'avg_price_per_room', 'no_of_special_requests', 'booking_status']

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    # Nao permitir menos que 1 adulto
    no_of_adults = st.number_input("Número de Adultos", step=1, min_value=1, value=1)

with col2:
    no_of_children = st.number_input("Número de Crianças", step=1)

with col3:
    no_of_weekend_nights = st.number_input("Número de Noites de Fim de Semana", step=1)

with col4:
    no_of_week_nights = st.number_input("Número de Noites de Semana", step=1)

with col5:
    type_of_meal_plan = st.selectbox(
        "Plano de Refeição",
        options=['Not Selected','Meal Plan 1', 'Meal Plan 2', 'Meal Plan 3']
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    required_car_parking_space = st.selectbox(
        "Necessita de Vaga de Estacionamento?",
        options=[1, 0],
        format_func=lambda x: "Sim" if x == 1 else "Não"
    )
with col2:
    room_type_reserved = st.selectbox(
        "Tipo de Quarto Reservado",
        options=['Room_Type 1', 'Room_Type 2', 'Room_Type 3', 'Room_Type 4',
       'Room_Type 5', 'Room_Type 6', 'Room_Type 7']
    )
with col3:
    lead_time = st.number_input("Tempo de Antecedência (dias)", step=1)

with col4:
    arrival_year = st.number_input("Ano de Chegada", step=1, min_value=2000, max_value=2025, value=2025)

    
col1, col2, col3, col4 = st.columns(4)

with col1:
    arrival_month = st.number_input("Mês de Chegada", step=1, min_value=1, max_value=12)

with col2:
    arrival_date = st.number_input("Dia de Chegada", step=1, min_value=1, max_value=31)

with col3:
    market_segment_type = st.selectbox(
        "Tipo de Segmento de Mercado",
        options=['Offline', 'Online', 'Corporate', 'Aviation', 'Complementary']
    )

with col4:
    repeated_guest = st.selectbox(
        "Hospede Repetido?",
        options=[1, 0],
        format_func=lambda x: "Sim" if x == 1 else "Não"
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    no_of_previous_cancellations = st.number_input("Número de Cancelamentos Anteriores", step=1, min_value=0)

with col2:
    no_of_previous_bookings_not_canceled = st.number_input("Número de Reservas Anteriores Não Canceladas", step=1, min_value=0)

with col3:
    avg_price_per_room = st.number_input("Preço Médio por Quarto (R$)", step=0.01, format="%.2f")

with col4:
    no_of_special_requests = st.number_input("Número de Pedidos Especiais", step=1, min_value=0)



dict_data = {
    "no_of_adults": no_of_adults,
    "no_of_children": no_of_children,
    "no_of_weekend_nights": no_of_weekend_nights,
    "no_of_week_nights": no_of_week_nights,
    "type_of_meal_plan": type_of_meal_plan,
    "required_car_parking_space": required_car_parking_space,
    "room_type_reserved": room_type_reserved,
    "lead_time": lead_time,
    "arrival_year": arrival_year,
    "arrival_month": arrival_month,
    "arrival_date": arrival_date,
    "market_segment_type": market_segment_type,
    "repeated_guest": repeated_guest,
    "no_of_previous_cancellations": no_of_previous_cancellations,
    "no_of_previous_bookings_not_canceled": no_of_previous_bookings_not_canceled,
    "avg_price_per_room": avg_price_per_room,
    "no_of_special_requests": no_of_special_requests
}


data = pd.DataFrame([dict_data])

if st.button("Fazer Previsão"):
    
    with st.spinner("Calculando..."):
        prediction = predict(data)
        if prediction is not None:
            if prediction == 1:
                # green color for high probability of cancellation
                st.markdown("<h3 style='color: red;'>A reserva tem alta probabilidade de ser cancelada.</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='color: green;'>A reserva tem baixa probabilidade de ser cancelada.</h3>", unsafe_allow_html=True)
        else:
            st.error("Erro na previsão. Verifique os dados ou tente novamente.")
