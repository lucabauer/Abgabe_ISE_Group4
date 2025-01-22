import csv
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

if __name__ == "__main__":
    csv_file = "FootballResults.csv"

    data = open_file(csv_file)


def transform_values():
    home_score = data["home_score"]
    away_score = data["away_score"]

    home_scores = [int(score) for score in home_score]
    away_scores = [int(score) for score in home_score]

