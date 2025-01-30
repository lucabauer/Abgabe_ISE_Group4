import plotly.graph_objects as go

def calculate_win_probabilities(matches, team1, team2):
    """Berechnet die Wahrscheinlichkeiten für Sieg, Niederlage und Unentschieden."""
    team1_wins = 0
    team2_wins = 0
    draws = 0

    for match in matches:
        if match["home_team"] == team1 and match["home_score"] > match["away_score"]:
            team1_wins += 1
        elif match["away_team"] == team1 and match["away_score"] > match["home_score"]:
            team1_wins += 1
        elif match["home_team"] == team2 and match["home_score"] > match["away_score"]:
            team2_wins += 1
        elif match["away_team"] == team2 and match["away_score"] > match["home_score"]:
            team2_wins += 1
        else:
            draws += 1

    total_matches = team1_wins + team2_wins + draws
    if total_matches == 0:
        return {"team1_win": 0, "team2_win": 0, "draw": 0}

    return {
        "team1_win": team1_wins / total_matches,
        "team2_win": team2_wins / total_matches,
        "draw": draws / total_matches,
    }

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
