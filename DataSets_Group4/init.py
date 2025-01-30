
from database import DatabaseConnector

if __name__ == "__main__":

    csv_file = "FootballResults.csv" #Name der CSV-Datei
    database_name = "International_matches.db" #Name der SQLite-Datenbank
    table_name = "matches" # Name der Tabelle in der Datenbank

    with DatabaseConnector(database_name) as db:
        #CSV-Daten importieren
        db.insert_csv_data_pandas(csv_file, table_name)

    print(f"Die Daten aus {csv_file} wurden erfolgreich in die Datenbank {database_name} importiert")