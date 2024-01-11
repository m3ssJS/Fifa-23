import streamlit as st
import pandas as pd
import plotly.express as px

# Carregando os dados
df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv')

# fonte dados ranking da IFFHS
# https://ge.globo.com/futebol/noticia/2023/10/12/fluminense-e-fortaleza-sobem-em-ranking-de-melhores-clubes-do-mundo-veja-lista.ghtml
clubes_interessados = [
    'Manchester City','Real Madrid CF', 'Inter', 'FC Porto', 'Al Ahly',
    'Manchester United', 'Fiorentina', 'Napoli', 'RB Leipzig', 'PSV', 'FC Bayern München', 
    'Benfica', 'Fenerbahçe SK', 'Juventus', 'Roma', 'Arsenal', 'FC Barcelona',
    'Royale Union Saint-Gilloise', 'Feyenoord', 'AC Milan', 'West Ham United'
    'Sevilla FC', 'Sporting CP', 'Paris Saint-Germain'
]

st.subheader('IFFHS (Federação Internacional de História e Estatística do Futebol)')

df_filtered = df_data[df_data['Club'].isin(clubes_interessados)]

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Valor de mercado - Total de Jogadores por Clube
fig1 = px.bar(df_filtered, x = "Value(£)", y = "Club", title = "Valor de mercado total do Clube")
col1.plotly_chart(fig1, use_container_width=True)

#----------------------------------------------------------------------------------------

# Supondo que 'df' é o seu DataFrame e que 'Overall' e 'Preferred Foot' são as colunas
destros = df_filtered[df_filtered['Preferred Foot'] == 'Right']['Overall']
canhotos = df_filtered[df_filtered['Preferred Foot'] == 'Left']['Overall']

media_destros = destros.mean()
media_canhotos = canhotos.mean()

# Criando o DataFrame para o gráfico
df_filtered = pd.DataFrame({
    'Pé Preferido': ['Right', 'Left'],
    'Média de Overall': [media_destros, media_canhotos]
})

# Criando o gráfico
fig2 = px.bar(df_filtered, x='Pé Preferido', y='Média de Overall', title='Média de Overall por Pé Preferido')
col2.plotly_chart(fig2, use_container_width=True)

#----------------------------------------------------------------------------------------

df_filtered = df_data[df_data['Club'].isin(clubes_interessados)]

fig3 = px.bar(df_filtered, x= "Wage(£)", y= "Club", title= "Total de Sálarios por Clube - Semanal")
col3.plotly_chart(fig3, use_container_width=True)

#----------------------------------------------------------------------------------------

media_overall_por_nacionalidade = df_data.groupby('Nationality')['Overall'].mean()

# Ordenando as nacionalidades pela média do overall em ordem decrescente e selecionando as 5 primeiras
media_overall_por_nacionalidade = media_overall_por_nacionalidade.sort_values(ascending=False).head(5)
fig4 = px.box(df_filtered, x= "Nationality", y= "Overall", title= "Média de Overall por Nacionalidade")
col4.plotly_chart(fig4, use_container_width=True)