import plotly.graph_objects as go

def plot_win_probabilities(probabilities, team1, team2):
    """Erstellt ein interaktives Tortendiagramm für die Wahrscheinlichkeiten der Spielergebnisse."""
    labels = [f"Sieg {team1}", "Unentschieden", f"Sieg {team2}"]
    values = [
        probabilities["team1_win"],
        probabilities["draw"],
        probabilities["team2_win"]
    ]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Blau, Orange, Grün

    fig = go.Figure(
        data=[go.Pie(
            labels=labels,
            values=values,
            marker=dict(colors=colors),
            textinfo="percent+label",
            hole=0.3  # Halbkreis-Effekt für eine moderne Darstellung (Optional)
        )]
    )

    fig.update_layout(
        title="Wahrscheinlichkeit für den Spielausgang",
        template="plotly_white"
    )
    return fig

def plot_team_record_pie_chart(record):
    """Erstellt ein Pie-Chart für die Bilanz eines Teams mit Plotly."""

    # Daten für das Diagramm
    labels = ['Siege', 'Unentschieden', 'Niederlagen']
    values = [record['Siege'], record['Unentschieden'], record['Niederlagen']]
    colors = ['#4CAF50', '#FFC107', '#F44336']  # Farben für die Segmente (Grün, Gelb, Rot)

    # Erstelle das Pie-Chart mit Plotly
    fig = go.Figure(
        data=[go.Pie(
            labels=labels,
            values=values,
            marker=dict(colors=colors),
            textinfo="percent+label",  # Zeige Prozent und Label an
            hole=0.3  # Halbkreis-Effekt für eine moderne Darstellung (Optional)
        )]
    )

    # Titel hinzufügen
    fig.update_layout(
        title="Bilanz des Teams",
        title_x=0.5  # Titel zentrieren
    )
    return fig