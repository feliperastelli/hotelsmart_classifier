# HotelSmart Classifier - Projeto Integrador - Pos Graduacao em Ciencia de Dados 🏨

## Contexto

Os canais de reserva de hotéis online transformaram a forma como os clientes fazem suas reservas. No entanto, isso trouxe um desafio significativo: um número considerável de reservas são canceladas.
Para a HotelSmart, a alta taxa de cancelamento representa um problema financeiro e operacional. Cada cancelamento tem um **custo médio estimado de R$3.500**. Com uma projeção de **50.000 reservas para o próximo ano**, a perda potencial é substancial.

### Objetivo

Desenvolver um modelo de Machine Learning capaz de **prever com alta acurácia se uma reserva de hotel será cancelada ou não**. 

O modelo permitirá à HotelSmart:
1.  **Adotar medidas proativas:** Como oferecer pequenos descontos, upgrades ou confirmar a intenção de estadia para reservas de alto risco de cancelamento.
2.  **Otimizar a gestão de ocupação:** Liberar quartos de reservas de alto risco para outros clientes.
3.  **Reduzir perdas financeiras** e aumentar a lucratividade.

## O que foi feito (visão macro)

- Coleta e pré-processamento de dados
- Engenharia de features
- Análise Exploratória
- Seleção de features com Boruta
- Treinamento de modelo de machine learning (ex.: Random Forest, XGBoost ou modelo de linguagem).
- Avaliação com Kfold Cross Validation e Fine Tuning com Bayesian Opt.
- Avaliação do modelo por meio de métricas (accuracy, precision, recall, f1-score).
- Deploy do modelo na nuvem usando **Koyeb**.
- Desenvolvimento de uma interface interativa com **Streamlit** para uso final por stakeholders.

## Hipóteses e Insights

- **Hipótese 1**: *O canal de reservas online apresenta maior taxa de cancelamento*
- **Hipótese 2**: *A taxa de cancelamento é menor para pessoas com histórico de não cancelamento*
- **Hipótese 3**: *O preço ofertado influencia na taxa de cancelamento*
- **Hipótese 4**: *Pessoas com crianças inclusas na reserva tendem a ter mais cancelamentos*
- **Hipótese 5**: *Quanto maior a antecipação da reserva maior a taxa de cancelamento*
- **Hipótese 6**: *Alguns meses (com feriados) possuem maior taxa de cancelamento*
- **Hipótese 7**: *Reservas com pedidos especiais são mais prováveis de serem confirmadas, pois indicam um maior engajamento do cliente*

**Insights encontrados** (preencha depois):

- Insight 1: O canal Online apresenta maior taxa de cancelamento de fato
- Insight 2: Não foi possível observar
- Insight 2: Preços mais altos tendem a maior probabilidade de cancelamento
- Insight 2: Sim, a proporção de reservas canceladas é maior
- Insight 2: Essa variável foi a mais relevante, pois de fato isso é verdade
- Insight 2: A flutução acontece, mas muito em fator do aumento de reservas também. Alguns meses sofrem menos cancelamentos.
- Insight 2: Sim, quando não há pedidos especiais, a taxa de cancelamento é maior, muito provavelmente pelo menor engajamento do cliente com o hotel.

## Resultados do modelo

**Métricas de desempenho**:

| Métrica   | Valor         |
| --------- | ------------- |
| Accuracy  | *0,87* |
| Precision | *0,84* |
| Recall    | *0,74* |

**Resultados Esperados de Negõcio**:

Dado que:

**Total de Reservas esperadas**: 50.000
**Taxa de cancelamento histórico**: 32%
**Custo médio de cancelamento**: 3.500

O modelo aplicado apresenta os seguintes resultadosÇ

- Cancelamentos esperados: 16000
- Cancelamentos previstos corretamente (TP): 11840
- Falsos positivos: 2255
- Economia potencial: R$ 41,440,000.00
- Perda potencial: R$ 7,893,333.33
- **💰 Economia líquida estimada: R$ 33,546,666.67**

---

## Deploy e Interface

O modelo foi **publicado com sucesso no Koyeb**, garantindo alta disponibilidade e escalabilidade.\
A interface interativa foi construída com **Streamlit**, permitindo aos usuários:

- Inserir ou colar avaliações de hotéis.
- Visualizar a classificação do modelo em tempo real.
- Explorar métricas e explicações adicionais (se aplicável).

---

## Como utilizar

Acesse a app, e preencha as inforções solicitadasÇ

https://feliperastelli-hotelsmart-classifier-app-streamlithome-zzead4.streamlit.app/

---

## Próximos passos

- Testar outros modelos de ML
- Refinar a engenharia de features e processamento dos dados
- Melhorar a interface da app, deixando possivelmente apenas a solicitação dos dados necessários para o modelo
  
---

## Autor

**Felipe Rastelli** – Desenvolvedor de Data Science\
[GitHub](https://github.com/feliperastelli)


