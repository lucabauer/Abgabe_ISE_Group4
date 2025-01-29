import csv
import pandas as pd
import sqlite3
import plotly.graph_objects as go

def open_file(file_name):
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)

        headers = file.readline().strip().split(",")
        print("Header:", headers)

        matches_dict = {header: [] for header in headers}

        for line in file:
            match_values = line.strip().split(",")
            for i, match_value in enumerate(match_values):
                matches_dict[headers[i]].append(match_value)

    return matches_dict

class DatabaseConnector:
    def __init__(
            self,
            database_name: str
    ) -> None:
        """
            Initialisiert den kontextmanager

        :param database_name: Name der Datenbank
        """
        self._database_name = database_name

    def __enter__(self):
        """
            Initialisiert die Datenbankverbindung und erstellt einen Cursor

        :return: Gibt den DatabaseConnector zurück
        """
        self._connection = sqlite3.connect(self._database_name) # Verbindung zur SQLite-Datenbank herstellen
        self._connection.row_factory = sqlite3.Row # Aktiviert benannte Indizes
        self._cursor = self._connection.cursor() # Cursor_Objekt erstellen, um SQL-Befehle auszuführen
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Schließt die Datenbankverbindung, wenn der Kontext verlassen wird
        """
        if self._connection:
            self._connection.close()  # Verbindung zur SQLite-Datenbank schließen

        if exc_type or exc_val or exc_tb:
            # Debugging: Ausnahmen können hier geloggt werden
            print(f"Exception occurred: {exc_type}, {exc_val}")

            # Keine Ausnahme unterdrücken; Standardverhalten übernehmen
        return False

def insert_csv_data_pandas(
            self,
            csv_path: str,
            table_name:str
        ):
        #CSv Datei mit pandas einlesen
        df = pd.read_csv(csv_path)

        #Daten in die SQLite-Datenbank schreiben
        df.to_sql(table_name, self._connection, if_exists="replace", index=False)
        self._connection.commit()

def get_unique_countries(database_name = "International_matches.db"):
    """Holt alle eindeutigen Länder aus den Spalten 'home_team' und 'away_team'."""
    query = """
        SELECT DISTINCT home_team AS team FROM matches
        UNION
        SELECT DISTINCT away_team AS team FROM matches
        ORDER BY team
        """
    with DatabaseConnector(database_name) as db:
        countries = db._cursor.execute(query)
        countries = [row["team"] for row in db._cursor.fetchall()]
        return countries

def get_matches_between_teams(team1, team2, database_name = "International_matches.db"):
    """Holt alle Spiele zwischen zwei Teams aus der Datenbank."""
    query = """
        SELECT * 
        FROM matches 
        WHERE (home_team = ? AND away_team = ?) OR (home_team = ? AND away_team = ?)
        """
    with DatabaseConnector(database_name) as db:
        games = db._cursor.execute(query, (team1, team2, team2, team1))
        games = db._cursor.fetchall()
        return games

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

if __name__ == "__main__":

    csv_file = "FootballResults.csv" #Name der CSV-Datei
    database_name = "International_matches.db" #Name der SQLite-Datenbank
    table_name = "matches" # Name der Tabelle in der Datenbank

    """with DatabaseConnector(database_name) as db:
        #CSV-Daten importieren
        db.insert_csv_data_pandas(csv_file, table_name)

    print(f"Die Daten aus {csv_file} wurden erfolgreich in die Datenbank {database_name} importiert")
    print("Ausgabe der ersten 5 Datensätze:")
    for row in data:
        print(row)"""

""" FUNKTIONIERT NICHT !!!!
    with DatabaseConnector(database_name) as db:
        result = db._cursor.execute("SELECT home_team FROM matches WHERE 'Germany'")
        print(result)
"""
"""
def transform_values():
    home_score = data["home_score"]
    away_score = data["away_score"]

    home_scores = [int(score) for score in home_score]
    away_scores = [int(score) for score in home_score]
"""
