import streamlit as st

pg = st.navigation([st.Page("pages/Startseite.py", title="🏠 Startseite"),
                    st.Page("pages/LaenderVergleich.py", title="🔄 Länder Vergleich"),
                    st.Page("pages/LaenderDetails.py", title="📋 Länder Details"),
                    st.Page("pages/TurnierAnalyse.py", title="🏆 Turnier Analyse"),
                    st.Page("pages/Account.py", title="👤 Account"),
                    st.Page("pages/Spenden.py", title="💰 Spenden")])
pg.run()