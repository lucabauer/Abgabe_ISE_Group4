import streamlit as st

from core.database import get_tournaments
from core.calculations import get_top_teams_by_tournament

st.title("🏆 Turnier-Analyse")

tournament = get_tournaments()
if tournament:
    tournament = st.selectbox(
        "Wähle ein Turnier",
        tournament,
        index=None,
        placeholder="Turnier"
    )
if tournament:
    result = get_top_teams_by_tournament(tournament)

    if isinstance(result, str):
        st.warning(result)
    else:
        st.subheader(f"📊 Top Teams in {tournament}")
        st.dataframe(result["Top Teams"])

        st.subheader("⚡ Höchster Sieg")
        st.write(result["Höchster Sieg"])

        st.subheader("⚽ Durchschnittliche Tore pro Spiel")
        st.write(result["Durchschnittliche Tore pro Spiel"])