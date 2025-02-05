import streamlit as st

def Startseite():
    st.title("⚽️ Football Result Predictor")
    st.write("Willkommen zu unserem interaktiven Fußball-Dashboard! Hier kannst du nicht nur vergangene Länderspiele eines Teams einsehen, sondern auch die Gewinnwahrscheinlichkeit zwischen zwei Teams berechnen.")
    st.write("✨ Funktionen:")
    st.write("📅 Alle Spiele eines Teams anzeigen – Wähle ein Team aus und erhalte eine Übersicht über alle vergangenen Begegnungen.")
    st.write("📊 Gewinnwahrscheinlichkeit berechnen – Vergleiche zwei Teams und erhalte eine Einschätzung darüber, welches Team die besseren Chancen auf den Sieg hat.")

    if st.button("Start"):
        st.switch_page("calculator.py")

    st.image("Stadion.jpg")

def all_games_of_country():
    st.title("Alle Spiele eines Landes")

pg = st.navigation([st.Page(Startseite), st.Page("calculator.py"), st.Page("AllGamesOfCountry.py"), st.Page("TurnierAnalyse.py")])
pg.run()

