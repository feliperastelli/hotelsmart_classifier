import streamlit as st

st.set_page_config(
    page_title="Análise de Cancelamento de Reservas",
    page_icon="🏠"
)

def main():
    st.title("Análise de Cancelamento de Reservas")
    st.write(
        """
            Bem-vindo ao aplicativo de previsão de cancelamento de reservas
            Este aplicativo utiliza um modelo de aprendizado de máquina para prever a probabilidade de cancelamento de uma reserva com base em dados históricos.
         """
    )
    st.write("Carregue seus dados e visualize os resultados.")

if __name__ == "__main__":
    main()