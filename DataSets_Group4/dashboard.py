import streamlit as st
import pandas as pd

from calculate_results import get_matches_between_teams
from calculate_results import get_unique_countries
from calculate_results import calculate_win_probabilities
from calculate_results import plot_win_probabilities

st.title("Football Result Predictor")

st.text("Hier kann man Vorhersagen zu Spielergebnissen sehen , "
        "die basierend auf vergangenen Spielen sind.")

countries = get_unique_countries()

if countries:
    team1 = st.selectbox(
        "Wähle Team 1",
        countries,
        index=None,
        placeholder = "Team 1",
    )

    team2 = st.selectbox(
        "Wähle Team 2",
        countries,
        index=None,
        placeholder="Team 2",
    )

    if team1 == team2:
        st.warning(
            "Bitte zwei unterschiedliche Teams auswählen!"
        )
    else:
        matches = get_matches_between_teams(team1, team2)

        if matches:

            probabilities = calculate_win_probabilities(matches, team1, team2)

            fig = plot_win_probabilities(probabilities, team1, team2)
            st.plotly_chart(fig)

            st.write(f"Wahrscheinlichkeit für {team1} zu gewinnen: {probabilities['team1_win']:.2%}")
            st.write(f"Wahrscheinlichkeit für {team2} zu gewinnen: {probabilities['team2_win']:.2%}")
            st.write(f"Wahrscheinlichkeit für ein Unentschieden: {probabilities['draw']:.2%}")

            # Zeige die Spiele, die für die Berechnungen verwendet wurden
            st.write(f"Hier sind alle erfassten Spiele zwischen {team1} und {team2}:")
            matches_df = pd.DataFrame(matches)  # Konvertiere die Spiele in ein Pandas DataFrame
            st.dataframe(matches_df)  # Zeige die Spiele als interaktive Tabelle an



        else:
            st.write("Keine Spiele zwischen diesen Teams gefunden.")
else:
    st.warning("Keine Länder in der Datenbank gefunden!")
