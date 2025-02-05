import plotly.graph_objects as go

import pandas as pd


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

def get_team_record(team, matches):
    """Berechnet die Anzahl der Siege, Niederlagen und Unentschieden eines Teams."""

    # Initialisiere Zähler
    wins = 0
    draws = 0
    losses = 0

    for match in matches:
        if team == match["home_team"]:  # Vergleiche das Team mit dem Heimteam
            if match["home_score"] > match["away_score"]:
                wins += 1
            elif match["home_score"] < match["away_score"]:
                losses += 1  # Niederlage als Heimteam
            else:
                draws += 1  # Unentschieden
        elif team == match["away_team"]:  # Vergleiche das Team mit dem Auswärtsteam
            if match["away_score"] > match["home_score"]:
                wins += 1  # Sieg als Auswärtsteam
            elif match["away_score"] < match["home_score"]:
                losses += 1  # Niederlage als Auswärtsteam
            else:
                draws += 1  # Unentschieden

    return {"Siege": wins, "Unentschieden": draws, "Niederlagen": losses}


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


def calculate_team_statistics(matches):
    """Berechnet Statistiken für jedes Team in einem Turnier und die durchschnittlichen Tore pro Spiel."""
    team_stats = {}
    total_goals = 0

    for match in matches:
        home_team, away_team = match["home_team"], match["away_team"]
        home_score, away_score = match["home_score"], match["away_score"]

        for team in [home_team, away_team]:
            if team not in team_stats:
                team_stats[team] = {"Punkte": 0, "Tore": 0, "Gegentore": 0, "Siege": 0, "Unentschieden": 0, "Niederlagen": 0}

        team_stats[home_team]["Tore"] += home_score
        team_stats[home_team]["Gegentore"] += away_score
        team_stats[away_team]["Tore"] += away_score
        team_stats[away_team]["Gegentore"] += home_score

        if home_score > away_score:
            team_stats[home_team]["Punkte"] += 3
            team_stats[home_team]["Siege"] += 1
            team_stats[away_team]["Niederlagen"] += 1
        elif home_score < away_score:
            team_stats[away_team]["Punkte"] += 3
            team_stats[away_team]["Siege"] += 1
            team_stats[home_team]["Niederlagen"] += 1
        else:
            team_stats[home_team]["Punkte"] += 1
            team_stats[away_team]["Punkte"] += 1
            team_stats[home_team]["Unentschieden"] += 1
            team_stats[away_team]["Unentschieden"] += 1

        total_goals += home_score + away_score

    avg_goals = round(total_goals / len(matches), 2) if matches else 0

    return team_stats, avg_goals


def get_best_teams(stats_dict):
    """Sortiert die Teams nach Punkten und gibt die Top-Teams zurück."""
    stats_df = pd.DataFrame.from_dict(stats_dict, orient="index")
    stats_df["Tordifferenz"] = stats_df["Tore"] - stats_df["Gegentore"]
    stats_df = stats_df.sort_values(by=["Punkte", "Tordifferenz", "Tore"], ascending=[False, False, False])

    return stats_df


def find_biggest_win(matches):
    """Findet das Spiel mit dem höchsten Sieg (größter Torunterschied)."""
    biggest_win = max(matches, key=lambda match: abs(match["home_score"] - match["away_score"]), default=None)
    if biggest_win:
        return f"{biggest_win['home_team']} {biggest_win['home_score']} - {biggest_win['away_score']} {biggest_win['away_team']}"
    return "Keine Daten verfügbar"

from database import get_matches_by_tournament



def get_top_teams_by_tournament(tournament_name, database_name="International_matches.db"):
    """Gibt eine umfassende Turnieranalyse zurück."""
    matches = get_matches_by_tournament(tournament_name, database_name)

    if not matches:
        return "Keine Daten für dieses Turnier gefunden."

    team_stats, avg_goals = calculate_team_statistics(matches)
    top_teams = get_best_teams(team_stats)
    biggest_win = find_biggest_win(matches)

    return {
        "Top Teams": top_teams,
        "Höchster Sieg": biggest_win,
        "Durchschnittliche Tore pro Spiel": avg_goals
    }

