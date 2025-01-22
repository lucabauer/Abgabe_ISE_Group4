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

    def __exit__(self, database_name):
        """
            Schließt die Datenbankverbindung, wenn der Kontext verlassen wird
        """
        self._connection.close() # Verbindung zur SQLite-Datenbank schließen

if __name__ == "__main__":
    csv_file = "FootballResults.csv"

    data = open_file(csv_file)


def transform_values():
    home_score = data["home_score"]
    away_score = data["away_score"]

    home_scores = [int(score) for score in home_score]
    away_scores = [int(score) for score in home_score]

