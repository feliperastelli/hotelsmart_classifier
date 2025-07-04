# HotelSmart Classifier 🏨

## Contexto

Este projeto visa construir um modelo de classificação para avaliações de hotéis, ajudando a identificar padrões e insights relevantes sobre a satisfação dos hóspedes. A aplicação principal é fornecer suporte automatizado na análise de texto, entregando previsões que auxiliam equipes de produto e marketing a entender melhor as necessidades dos usuários.

## O que foi feito (visão macro)

- Coleta e pré-processamento de dados de avaliações de hotéis.
- Engenharia de features textuais (limpeza, tokenização, vetorização).
- Treinamento de modelo de machine learning (ex.: Random Forest, XGBoost ou modelo de linguagem).
- Avaliação do modelo por meio de métricas (accuracy, precision, recall, f1-score).
- Deploy do modelo na nuvem usando **Koyeb**.
- Desenvolvimento de uma interface interativa com **Streamlit** para uso final por stakeholders.

## Hipóteses e Insights

- **Hipótese 1**: *(espaço para você preencher)*
- **Hipótese 2**: *(espaço para você preencher)*

**Insights encontrados** (preencha depois):

- Insight 1: …
- Insight 2: …

## Resultados do modelo

**Métricas de desempenho**:

| Métrica   | Valor         |
| --------- | ------------- |
| Accuracy  | *insira aqui* |
| Precision | *insira aqui* |
| Recall    | *insira aqui* |
| F1‑score  | *insira aqui* |

**Análise de Confusão**:\
*(incluir descrição ou imagem do confusion matrix)*

### Aplicação no Contexto

O modelo apresenta resultados consistentes com as expectativas do negócio, permitindo:

- Monitorar padrões nas avaliações dos hóspedes.
- Destacar aspectos positivos e negativos com base na classificação automática.
- Fornecer respostas rápidas a potenciais crises (ex.: aumento de avaliações negativas).
- Apoiar tomadas de decisão com dados reais e atualizados.

---

## Deploy e Interface

O modelo foi **publicado com sucesso no Koyeb**, garantindo alta disponibilidade e escalabilidade.\
A interface interativa foi construída com **Streamlit**, permitindo aos usuários:

- Inserir ou colar avaliações de hotéis.
- Visualizar a classificação do modelo em tempo real.
- Explorar métricas e explicações adicionais (se aplicável).

---

## Como utilizar

1. Clone o repositório:
   ```bash
   git clone https://github.com/feliperastelli/hotelsmart_classifier.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o app Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Acesse a interface no navegador e interaja com o modelo.

---

## Estrutura do Projeto

```
hotelsmart_classifier/
├── data/               # Dados brutos e pré-processados
├── notebooks/          # Análises exploratórias
├── src/                # Módulos de processamento e modelagem
├── app.py              # Interface principal do Streamlit
└── requirements.txt    # Dependências do projeto
```

---

## Próximos passos

- Testar o modelo com dados em produção.
- Refinar com feedback dos usuários.
- Automatizar atualizações com pipeline CI/CD.
- Expandir para suporte multilíngue e outros tipos de classificação.

---

## Autor

**Felipe Rastelli** – Desenvolvedor de Data Science\
[GitHub](https://github.com/feliperastelli)

