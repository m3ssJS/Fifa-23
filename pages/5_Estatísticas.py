import streamlit as st
import statistics as est
import pandas as pd

st.set_page_config(
    page_title="Estatísticas",
    page_icon="📈",
    layout="wide"
)

df_data = st.session_state["data"]

# Sidebar para selecionar o clube
selected_club = st.sidebar.selectbox("Selecione um clube", df_data["Club"].unique())

# Seletor para escolher o tipo de dados
selected_data_type = st.sidebar.selectbox("Selecione o tipo de dados", df_data.columns)

# Filtrando os dados do clube selecionado
club_data = df_data[df_data["Club"] == selected_club]

# Exibição das estatísticas do clube selecionado
if not club_data.empty:
    st.title(f"Estatísticas do Clube: {selected_club}")

    # Verificando se a coluna selecionada para exibir estatísticas contém dados numéricos
    if df_data[selected_data_type].dtype in ['int64', 'float64']:
        st.subheader(f"Estatísticas de {selected_data_type}")
        st.write(f"Média: {club_data[selected_data_type].mean():,}")
        st.write(f"Moda: {club_data[selected_data_type].mode().values[0]:,}")
        st.write(f"Mediana: {club_data[selected_data_type].median():,}")
        st.write(f"Desvio Padrão: {est.stdev(club_data[selected_data_type]):.2f}")
    else:
        st.write("Não é possível calcular estatísticas. Selecione uma coluna numérica.")

#----------------------------------------------------------------------------------------
st.divider()

salario_total = df_data['Wage(£)'].sum()
st.metric(label="Salário do plantel mundial semanalmente", value=f"£ {salario_total:,}")

salarios_por_clube = df_data.groupby('Club')['Wage(£)'].sum()
salarios_por_clube = salarios_por_clube.sort_values(ascending=False).head(3)

salarios_por_clube = salarios_por_clube.rename('Salários')

st.subheader("Os três clubes com maiores salários semanais")

#for Club in salarios_por_clube.index:
st.write(salarios_por_clube)

#----------------------------------------------------------------------------------------
st.divider()

st.subheader("As cinco nacionalidades com os jogadores mais valiosos")

# Agrupar por nacionalidade e somar os valores de mercado
soma_valores = df_data.groupby('Nationality')['Value(£)'].sum()

# Obter as 5 nacionalidades com a maior soma de valores de mercado
soma_valores_top_5 = soma_valores.nlargest(5)

# Exibir as 5 principais nacionalidades e suas somas de valores de mercado
st.write(soma_valores_top_5)
