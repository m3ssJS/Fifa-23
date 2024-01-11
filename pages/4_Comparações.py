import streamlit as st

st.set_page_config(
    page_title="Comparison",
    page_icon="↔️",
    layout="wide"
)

df_data = st.session_state["data"]

with st.sidebar:
    st.header("Jogador 1")
    clubes_jogador_1 = df_data["Club"].unique()  # Obter clubes únicos para o Jogador 1
    club_jogador_1 = st.selectbox("Clube do Jogador 1", clubes_jogador_1)

    # Filtrar jogadores com base no clube selecionado para o Jogador 1
    players_jogador_1 = df_data[df_data["Club"] == club_jogador_1]["Name"].unique()
    player1 = st.selectbox("Jogador 1", players_jogador_1)

with st.sidebar:
    st.header("Jogador 2")
    clubes_jogador_2 = df_data["Club"].unique()  # Obter clubes únicos para o Jogador 2
    club_jogador_2 = st.selectbox("Clube do Jogador 2", clubes_jogador_2)

    # Filtrar jogadores com base no clube selecionado para o Jogador 2
    players_jogador_2 = df_data[df_data["Club"] == club_jogador_2]["Name"].unique()
    player2 = st.selectbox("Jogador 2", players_jogador_2)

player_stats1 = df_data[df_data["Name"] == player1].iloc[0]
player_stats2 = df_data[df_data["Name"] == player2].iloc[0]

col1, col2 = st.columns(2)

# Exibindo informações do Jogador 1
with col1:
    st.image(player_stats1["Photo"])
    st.title(f"{player_stats1['Name']}")
    st.markdown(f"**Clube:** {player_stats1['Club']}")
    st.markdown(f"**Posição:** {player_stats1['Position']}")
    st.markdown(f"**Overall:** {player_stats1['Overall']}")
    st.progress(int(player_stats1['Overall']))
    st.markdown(f"**Valor de Mercado:** £{player_stats1['Value(£)']:,}")

# Exibindo informações do Jogador 2
with col2:
    st.image(player_stats2["Photo"])
    st.title(f"{player_stats2['Name']}")
    st.markdown(f"**Clube:** {player_stats2['Club']}")
    st.markdown(f"**Posição:** {player_stats2['Position']}")
    st.markdown(f"**Overall:** {player_stats2['Overall']}")
    st.progress(int(player_stats2['Overall']))
    st.markdown(f"**Valor de Mercado:** £{player_stats2['Value(£)']:,}")
