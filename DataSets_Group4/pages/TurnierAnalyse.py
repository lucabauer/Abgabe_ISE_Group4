import streamlit as st

from core.database import get_tournaments
from core.calculations import get_top_teams_by_tournament

#Cedric
st.title("🏆 Turnier-Analyse")

st.markdown(
    """
    Wähle ein Turnier und entdecke die Statistiken aller teilnehmenden Teams!  

    **🔹 Alle Teams im Überblick**  
    Eine Liste zeigt dir alle Mannschaften, die jemals an diesem Turnier teilgenommen haben.  

    **🔹 Punkte & Leistung**  
    Jedes Team erhält für seine Leistungen Punkte nach dem klassischen System:  
    - ✅ **Sieg:** 3 Punkte  
    - 🤝 **Unentschieden:** 1 Punkt  
    - ❌ **Niederlage:** 0 Punkte  

    **🔹 Detaillierte Statistiken**  
    Für jedes Team werden außerdem die erzielten Tore ⚽, die Gegentore ❌ und die Tordifferenz 📊 angezeigt.  

    Vergleiche die erfolgreichsten Nationen und finde heraus, wer die beste Bilanz in der Turniergeschichte hat! 🚀  
    """
)

#Cedric
tournament = get_tournaments()
if tournament:
    tournament = st.selectbox(
        "Wähle ein Turnier",
        tournament,
        index=None,
        placeholder="Turnier"
    )

#Luca
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