import streamlit as st

def startseite():
    st.title("⚽ Willkommen zur Fußball-Statistik-App 📊🏆")

    st.markdown(
        """  
        Entdecke spannende Fußballstatistiken und analysiere die Erfolge verschiedener Teams! Diese App bietet dir umfassende Einblicke in die Ergebnisse, Turniere und Vergleiche zwischen Nationalmannschaften.  

        ### 🔍 Was kannst du hier machen?  

        **🏅 Ländervergleich:**  
        Vergleiche zwei Nationalmannschaften und sieh dir ihre bisherigen Duelle an. Ein übersichtliches Kreisdiagramm 🥧 zeigt dir die Anzahl der Siege 🏆, Unentschieden 🤝 und Niederlagen ❌.  

        **📊 Team-Statistiken:**  
        Wähle eine Nationalmannschaft und analysiere ihre Gesamtbilanz. Entdecke alle Turnierteilnahmen, Siege, Niederlagen, Tore ⚽ und Gegentore.  

        **🏆 Turnier-Statistiken:**  
        Wähle ein Turnier und sieh dir alle Teams an, die jemals daran teilgenommen haben. Erfahre, wie viele Punkte sie gesammelt haben und vergleiche ihre Leistungen basierend auf Toren und Tordifferenzen.  

        Nutze diese Daten, um tiefere Einblicke in die Fußballgeschichte zu gewinnen und spannende Trends zu entdecken! 🚀  
        """
    )
    st.image("static/Stadion.jpg")

pg = st.navigation([st.Page(startseite, title= "🏠 Startseite"),
                    st.Page("pages/calculator.py", title="🔄 Länder Vergleich"),
                    st.Page("pages/AllGamesOfCountry.py", title="📋 Länder Details"),
                    st.Page("pages/TurnierAnalyse.py", title="🏆 Turnier Analyse")])
pg.run()