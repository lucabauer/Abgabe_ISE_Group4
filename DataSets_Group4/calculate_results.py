import csv
import pandas as pd
import sqlite3

# Test

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

    def fetch_data(self, table_name: str, limit: int = 10):
        """
            Ruft eine begrenzte Anzahl von Zeilen aus der angegebenen Tabelle ab.

            :param table_name: Name der Tabelle in der Datenbank
            :param limit: Anzahl der Zeilen, die abgerufen werden sollen (Standard: 10)
            :return: Abgerufene Daten als Liste von Tupeln
        """
        self._cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
        return self._cursor.fetchall()


if __name__ == "__main__":
    csv_file = "FootballResults.csv" #Name der CSV-Datei
    database_name = "International_matches.db" #Name der SQLite-Datenbank
    table_name = "matches" # Name der Tablle in der Datenbank

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
