import streamlit as st

st.title("👤 Mein Account")

st.write("Hier kannst du deinen Account verwalten!")

st.text_input("Login Name")
st.text_input("Passwort", type="password")


if  st.button("Login"):
    st.write("Diese Funktion funktioniert leider noch nicht! 😕")

if st.button("Account erstellen"):
    st.write("Diese Funktion funktioniert leider noch nicht! 😕")

