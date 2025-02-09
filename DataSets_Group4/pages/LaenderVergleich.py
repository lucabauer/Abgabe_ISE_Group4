import pandas as pd
import streamlit as st

from core.calculations import calculate_head_to_head_stats
from core.visualizations import  plot_head_to_head_stats
from core.database import get_matches_between_teams, get_unique_countries

#Cedric

st.title("🔄 Länder Vergleich")

st.markdown(
    """  
    Vergleiche zwei Nationalmannschaften und entdecke ihre bisherige Bilanz!  

    **🔹 Alle direkten Duelle auf einen Blick**  
    In der übersichtlichen Tabelle 📋 findest du alle Spiele, die die beiden Teams gegeneinander bestritten haben – inklusive Ergebnisse und Details.  

    **🔹 Anschauliches Kreisdiagramm**  
    Das Diagramm 🥧 zeigt dir auf einen Blick, wie oft eine Mannschaft gewonnen 🏆, unentschieden gespielt 🤝 oder verloren ❌ hat.  

    Analysiere die Statistiken und finde heraus, welches Team historisch die Nase vorn hat! 🚀  
    """
)

#Oliver
countries = get_unique_countries()

if countries:
    team1 = st.selectbox(
        "Wähle Team 1",
        countries,
        index=None,
        placeholder="Team 1"
    )

    team2 = st.selectbox(
        "Wähle Team 2",
        countries,
        index=None,
        placeholder = "Team 2"
    )

    if team1 == team2:
        st.warning(
            "Bitte zwei unterschiedliche Teams auswählen!"
        )
    else:
        matches = get_matches_between_teams(team1, team2)

        if matches:

            head_to_head_stats = calculate_head_to_head_stats(matches, team1, team2)

            #Cedric (
            fig = plot_head_to_head_stats(head_to_head_stats, team1, team2)
            st.plotly_chart(fig)
            #)

            st.write(f"{team1} hat {head_to_head_stats['team1_win']:.2%} der Spiele gewonnen")
            st.write(f"{team2} hat {head_to_head_stats['team2_win']:.2%} der Spiele gewonnen")
            st.write(f"Es wurde {head_to_head_stats['draw']:.2%} Unentschieden gespielt")

            # Zeige die Spiele, die für die Berechnungen verwendet wurden
            st.write(f"Hier sind alle erfassten Spiele zwischen {team1} und {team2}:")
            matches_df = pd.DataFrame(matches)  # Konvertiere die Spiele in ein Pandas DataFrame
            st.dataframe(matches_df)  # Zeige die Spiele als interaktive Tabelle an

        else:
            st.write("Keine Spiele zwischen diesen Teams gefunden.")
else:
    st.warning("Keine Länder in der Datenbank gefunden!")
