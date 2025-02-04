import streamlit as st

def startseite():
    st.title("Football Result Predictor")
    st.write("Hier kann man Vorhersagen zu Spielergebnissen sehen , "
        "die basierend auf vergangenen Spielen sind.")

    if st.button("Start"):
        st.switch_page("calculator.py")

def calculation():
    st.title("Rechner")

def AllGamesOfCountry():
    st.title("Alle Spiele eines Landes")

pg = st.navigation([st.Page(startseite), st.Page("calculator.py"), st.Page("AllGamesOfCountry.py")])
pg.run()

