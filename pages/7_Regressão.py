import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Carregando os dados
df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv')  # Caminho do arquivo

# Selecionando as colunas para a regressão
X = df_data[['Value(£)']].values  # 'coluna1'
y = df_data['Wage(£)'].values  # 'coluna2'

# Instanciando o modelo de regressão linear
model = LinearRegression()

# Treinando o modelo com os dados
model.fit(X, y)

# Criando um campo de entrada de texto para o valor que o usuário deseja prever
user_input = st.text_input("Digite o valor de mercado do jogador que você deseja prever o salário (e aperte ENTER):")

# Verificando se o usuário digitou algo
if user_input:
    # Convertendo a entrada do usuário para um número
    user_input = float(user_input)

    # Realizando previsões
    X_test = np.array([[user_input]])  # Valores que deseja prever
    predictions = model.predict(X_test)

    # Imprimindo as previsões
    st.write("Previsão de salário:", predictions)
