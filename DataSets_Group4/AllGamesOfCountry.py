import streamlit as st
import pandas as pd
from database import get_unique_countries
from database import get_matches_by_team

st.title("📊 Länderspiele anzeigen")

countries = get_unique_countries()

# Falls Länder vorhanden sind, eine Selectbox anzeigen
if countries:
    team = st.selectbox(
        "Wähle Team 1",
        countries,
        index=None,
        placeholder="Team 1",
    )

    # Wenn ein Team ausgewählt wurde, spiele anzeigen
    if team:
        matches = get_matches_by_team(team)

        # Prüfen, ob die Liste 'matches' leer ist
        if matches:

            st.write(f"Hier sind alle Spiele von {team}")
            matches_df = pd.DataFrame(matches)  # Konvertiere die Spiele in ein Pandas DataFrame
            st.dataframe(matches_df)  # Zeige die Spiele als interaktive Tabelle an

        else:
            st.warning("Keine Spiele für dieses Land gefunden.")
else:
    st.warning("⚠️ Keine Länder in der Datenbank gefunden!")
