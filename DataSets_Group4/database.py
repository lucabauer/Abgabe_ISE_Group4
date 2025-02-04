import sqlite3
import pandas as pd

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
            table_name: str
    ):
        # CSv Datei mit pandas einlesen
        df = pd.read_csv(csv_path)

        # Daten in die SQLite-Datenbank schreiben
        df.to_sql(table_name, self._connection, if_exists="replace", index=False)
        self._connection.commit()


def get_unique_countries(database_name="International_matches.db"):
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


def get_matches_between_teams(team1, team2, database_name="International_matches.db"):
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

def get_matches_by_team(team, database_name="International_matches.db"):
    """Holt alle Spiele eines Teams aus der Datenbank (egal ob Heim- oder Auswärtsspiel)."""
    query = """
        SELECT * 
        FROM matches 
        WHERE home_team = ? OR away_team = ?
        ORDER BY date DESC
        """

    with DatabaseConnector(database_name) as db:
        games= db._cursor.execute(query, (team, team))
        games = db._cursor.fetchall()
        return games
