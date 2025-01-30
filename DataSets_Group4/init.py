import pandas as pd
import sqlite3

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
