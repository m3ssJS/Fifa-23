import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

# Dicionário de mapeamento
column_mapping = {
    "Age": "Idade",
    "Photo": "Foto",
    "Flag": "Bandeira",
    "Overall": "Geral",
    "Value(£)": "Valor(£)",
    "Wage(£)": "Salário(£)",
    "Joined": "Ingressou",
    "Height(cm.)": "Altura(cm.)",
    "Weight(lbs.)": "Peso(lbs.)",
    "Contract Valid Until": "Contrato válido até",
    "Release Clause(£)": "Cláusula de rescisão(£)"
}

# Renomeando as colunas
df_filtered.rename(columns=column_mapping, inplace=True)

# Atualizando a lista de colunas para exibir
columns = list(column_mapping.values())

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

st.dataframe(df_filtered[columns],
            column_config={
                    "Geral": st.column_config.ProgressColumn("Geral", format="%d", min_value=0, max_value=100),
                    "Valor(£)": st.column_config.NumberColumn(),
                    "Salário(£)": st.column_config.ProgressColumn("Salário Semanal", format="£%f",
                                                    min_value=0, max_value=df_filtered["Salário(£)"].max()),
                    "Foto": st.column_config.ImageColumn(),
                    "Bandeira": st.column_config.ImageColumn("País"),
            }, height=1000)
