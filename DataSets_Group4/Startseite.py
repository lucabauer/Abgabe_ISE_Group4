import streamlit as st

def startseite():
    st.title("Football Result Predictor")

st.sidebar.title("Navigation")

def calculation():
    st.title("Rechner")

pg = st.navigation([st.Page(startseite), st.Page("calculator.py")])
pg.run()

st.write("Hier kann man Vorhersagen zu Spielergebnissen sehen , "
        "die basierend auf vergangenen Spielen sind.")

if st.button("Start"):
    st.switch_page("calculator.py")