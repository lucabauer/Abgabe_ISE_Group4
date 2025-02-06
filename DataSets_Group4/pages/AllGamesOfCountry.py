import streamlit as st
import pandas as pd

from core.calculations import get_team_record, get_team_tournament_performance
from core.database import get_unique_countries, get_matches_by_team, get_matches_by_tournament
from core.visualizations import plot_team_record_pie_chart

st.title("📊 Länderspiele anzeigen")

countries = get_unique_countries()

# Falls Länder vorhanden sind, eine Selectbox anzeigen
if countries:
    team = st.selectbox(
        "Wähle ein Team ",
        countries,
        index=None,
        placeholder="Team ",
    )

    # Wenn ein Team ausgewählt wurde, Bilanz zuerst anzeigen
    if team:
        matches = get_matches_by_team(team)

        if matches:
            record = get_team_record(team, matches)

            st.write(f"🏆 **Bilanz von {team}:**")
            st.write(f"✅ **Siege:** {record['Siege']}")
            st.write(f"➖ **Unentschieden:** {record['Unentschieden']}")
            st.write(f"❌ **Niederlagen:** {record['Niederlagen']}")

            # Danach die Visualisierung
            fig = plot_team_record_pie_chart(record)
            st.plotly_chart(fig)

            # Danach Turnierleistung anzeigen
            tournament_performance = get_team_tournament_performance(team)

            if tournament_performance:
                st.write(f"📋 **Turnier-Performance von {team}:**")
                performance_df = pd.DataFrame(tournament_performance)
                performance_df["Spiele"] = performance_df["Siege"] + performance_df["Unentschieden"] + performance_df["Niederlagen"]

                st.dataframe(performance_df)  # Tabelle mit Turnierleistung anzeigen
            else:
                st.warning(f"Keine Turnier-Daten für {team} gefunden.")

            # Danach alle Spiele des Teams anzeigen
            st.write(f"Hier sind alle Spiele von {team}")
            matches_df = pd.DataFrame(matches)  # Konvertiere die Spiele in ein Pandas DataFrame
            st.dataframe(matches_df)  # Zeige die Spiele als interaktive Tabelle an
        else:
            st.warning("Keine Spiele für dieses Land gefunden.")
else:
    st.warning("⚠️ Keine Länder in der Datenbank gefunden!")
