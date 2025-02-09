import sqlite3
import pandas as pd

#Luca
class DatabaseConnector:
    def __init__(self,database_name: str) -> None:
        """
            Initialisiert den kontextmanager

        :param database_name: Name der Datenbank
        """
        self._database_name: str = database_name

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

    def insert_csv_data_pandas(self, csv_path: str, table_name: str) -> None:
        """
        Liest eine CSV Datei ein und speichert die Daten als Tabelle in die SQLite Datenbank.

        :param csv_path: Pfad zur CSV Datei
        :param: Name der Tabelle
        """

        # CSv Datei mit pandas einlesen
        df = pd.read_csv(csv_path)

        # Daten in die SQLite-Datenbank schreiben
        df.to_sql(table_name, self._connection, if_exists="replace", index=False)
        self._connection.commit()

#Oliver
#Ruft eindeutige Länder aus der DB ab
def get_unique_countries(database_name: str ="International_matches.db"):
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

#Luca
#Sucht alle Turniere aus der DB
def get_tournaments(database_name: str ="International_matches.db"):
    """Holt alle einzigartigen Turniernamen aus der Datenbank."""
    query = """
        SELECT DISTINCT tournament 
        FROM matches
        ORDER BY tournament
    """

    with DatabaseConnector(database_name) as db:
        tournaments = db._cursor.execute(query)
        tournaments = [row["tournament"] for row in db._cursor.fetchall()]
        return tournaments

#Oliver
#Sucht Spiele zwischen zwei Ländern aus der DB
def get_matches_between_teams(team1: str, team2: str, database_name: str="International_matches.db"):
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

#Victor
#Sucht alle Spiele die ein Land gespielt hat
def get_matches_by_team(team: str, database_name: str ="International_matches.db"):
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

#Luca
#Sucht alle Spiele eines Turniers
def get_matches_by_tournament(tournament_name: str, database_name: str="International_matches.db"):
    """Holt alle Spiele eines bestimmten Turniers aus der Datenbank."""
    query = """
        SELECT * 
        FROM matches 
        WHERE tournament = ?
        ORDER BY date ASC
        """

    with DatabaseConnector(database_name) as db:
        games = db._cursor.execute(query, (tournament_name,))
        games = db._cursor.fetchall()
        return games

#Victor
#Sucht alle Turniere, an den ein Team teilgenommen hat.
def get_tournaments_by_team(team: str, database_name: str="International_matches.db"):
    """Holt alle Turniere, an denen ein Team teilgenommen hat."""
    query = """
        SELECT DISTINCT tournament 
        FROM matches
        WHERE home_team = ? OR away_team = ?
        ORDER BY tournament
    """
    with DatabaseConnector(database_name) as db:
        tournaments = db._cursor.execute(query, (team, team))
        tournaments = [row["tournament"] for row in db._cursor.fetchall()]
        return tournaments