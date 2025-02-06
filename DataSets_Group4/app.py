import streamlit as st

def startseite():
    st.title("⚽️ Football Result Predictor")
    st.write("Willkommen zu unserem interaktiven Fußball-Dashboard! Hier kannst du nicht nur vergangene Länderspiele eines Teams einsehen, sondern auch die Gewinnwahrscheinlichkeit zwischen zwei Teams berechnen.")
    st.write("✨ Funktionen:")
    st.write("📅 Alle Spiele eines Teams anzeigen – Wähle ein Team aus und erhalte eine Übersicht über alle vergangenen Begegnungen.")
    st.write("📊 Gewinnwahrscheinlichkeit berechnen – Vergleiche zwei Teams und erhalte eine Einschätzung darüber, welches Team die besseren Chancen auf den Sieg hat.")
    st.image("static/Stadion.jpg")

pg = st.navigation([st.Page(startseite, title= "🏠 Startseite"),
                    st.Page("pages/calculator.py", title="🔄 Länder Vergleich"),
                    st.Page("pages/AllGamesOfCountry.py", title="📋 Länder Details"),
                    st.Page("pages/TurnierAnalyse.py", title="🏆 Turnier Analyse")])
pg.run()