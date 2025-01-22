#Aufgabe 1

def open_file(file_name):
    # Datei öffnen
    with open(file_name, mode="r") as file:
        # Erste Zeile als Header lesen und in eine Liste umwandeln
        headers = file.readline().strip().split(";")

        # Initialisiere das Dictionary mit leeren Listen für jeden Header
        values_dict = {header: [] for header in headers}

        # Jede weitere Zeile einlesen und die Werte den Listen in values_dict hinzufügen
        for line in file:
            # Zeile in Werte aufteilen
            values = line.strip().split(";")
            for i, value in enumerate(values):
                values_dict[headers[i]].append(value)

    return values_dict


if __name__ == "__main__":
    csv_file = "FinancialSample.csv"

    data = open_file(csv_file)

    #Alle Daten Ausgeben
    #print(data)

    #Ausgabe eines Teils der Daten

    print("\nAufgabe 1:")
    for key, values in data.items():
        print(f"{key}: {values[:5]} ...")

    #Spalte "Units Sold"
    units_sold = data["Units Sold"]

#Aufgabe 2

    #Werte in float umwandeln
    units_sold = [float(value.replace(",",".")) for value in units_sold]

    # Kleinster, höchter und Durchschnittswert berechnen
    min_units = min(units_sold)
    max_units = max(units_sold)
    avg_units = sum(units_sold) / len(units_sold)

    #Runden von Durschnitt
    avg_units = round(avg_units, 2)

    #Ausgabe der Ergebnisse
    print("\nAufgabe 2: ")
    print(f"Kleinster Wert von Units Sold: {min_units}")
    print(f"Höchster Wert von Units Sold: {max_units}")
    print(f"Durchschnittswert von Units Sold: {avg_units}")

# Aufgabe 3

    # Spalten, die Dollar-Werte enthalten (z.B. "Gross Sales", "Sale Price", etc.)
dollar_columns = ["Manufacturing Price ", " Sale Price ", " Gross Sales ", " Discounts ", " Sales ", " COGS "," Profit "]


def convert_to_euro(value):
    """
    Funktion konvertiert einen Dollar-Wert in Euro.
    """
    try:
        # Bereinigen: $ entfernen, Dezimal- und Tausendertrennzeichen anpassen
        value = value.replace("$", "").replace(".", "").replace(",", ".").strip()
        # Leere Werte oder '-' werden als 0.0 interpretiert
        if value == "" or value == "-":
            return 0.0
        # In Float umwandeln und in Euro konvertieren
        # Es wird auf 2 Dezimalstellen gerundet
        return round(float(value) , 2)
    except ValueError:
        # Falls ein Fehler auftritt (unerwartetes Format), 0.0 zurückgeben
        return 0.0


#Überprüft jede Spalte in der Liste
for column in dollar_columns:
    if column in data:
        #Nur wenn die Spalte in den Daten existiert.
        #Konvertiert die Werte in der Spalte in Euro
        converted_values = [
            convert_to_euro(value) for value in data[column]
        ]
        # Speichert die neuen Werte und fügt "€" hinzu.
        data[column] = [f"{value:.2f} €" for value in converted_values]

    # Bereinigte und konvertierte Werte ausgeben
print("\nAufgabe 3:")
print("Bereinigte und konvertierte Daten (in €):")
for column in dollar_columns:
    if column in data:
        # Nur wenn die Spalte existiert
        # Zeigt die ersten 10 Werte der Spalte.
        print(f"{column} (in €): {data[column][:10]} ...")

# Aufgabe 4:
    # Anzahl der Zeilen für bestimmte Bedingungen ermitteln

    # Anzahl der Zeilen für das Jahr 2013
year_2013_count = sum(1 for year in data["Year"] if year.strip() == "2013")

    # Anzahl der Zeilen für das Jahr 2014
year_2014_count = sum(1 for year in data["Year"] if year.strip() == "2014")

        # Anzahl der Zeilen ohne Discount
no_discount_count = sum(1 for discount in data[" Discount Band "] if discount.strip().lower() == "none")

    # Ergebnisse ausgeben
print("\nAufgabe 4:")
print(f"a. Anzahl der Zeilen für das Jahr 2013: {year_2013_count}")
print(f"b. Anzahl der Zeilen für das Jahr 2014: {year_2014_count}")
print(f"c. Anzahl der Zeilen ohne Discount: {no_discount_count}")

#Aufgabe 5

    # Dictionary, das Monatsnamen ihren numerischen Werten zuordnet
month_name_to_number = {
        "January": "1", "February": "2", "March": "3", "April": "4",
        "May": "5", "June": "6", "July": "7", "August": "8",
        "September": "9", "October": "10", "November": "11", "December": "12"
    }

if " Month Name " in data:
    # Ersetze Monatsnamen durch ihre numerischen Äquivalente
    data[" Month Name "] = [
        month_name_to_number.get(month.strip(), month.strip())  # Ersetze, falls im Dictionary vorhanden
        for month in data[" Month Name "]
    ]
    # Ausgabe

print("\nAufgabe 5:")
print(f"{data[' Month Name '][:10]} ...")  # Beispielhafte Ausgabe der ersten 10 Einträge