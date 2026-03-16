import csv

file_path = "python-works\Tasks\Jan-05\country_wise_latest_covid.csv"

fr = open(file_path, "r", encoding="utf-8")

reader = csv.DictReader(fr)

data = [row for row in reader]


# 1 . all unique WHO regions

regions = { line.get("WHO Region") for line in data }

print("WHO Regions :", regions)


# 2 . country with highest confirmed cases

max_confirmed = 0

max_country = None

for line in data :

    confirmed = int(line.get("Confirmed"))

    if confirmed > max_confirmed :

        max_confirmed = confirmed

        max_country = line.get("Country/Region")

print("\nHighest confirmed cases :", max_country, max_confirmed)


# 3 . countries with death rate greater than 5

print("\nCountries with Deaths / 100 Cases > 5 :")

for line in data :

    death_rate = float(line.get("Deaths / 100 Cases"))

    if death_rate > 5 :

        print(line.get("Country/Region"), death_rate)


# 4 . total new cases reported

total_new_cases = 0

for line in data :

    total_new_cases += int(line.get("New cases"))

print("\nTotal new cases :", total_new_cases)


# 5 . country with highest 1 week % increase

max_increase = 0

inc_country = None

for line in data :

    increase = float(line.get("1 week % increase"))

    if increase > max_increase :

        max_increase = increase

        inc_country = line.get("Country/Region")

print("\nHighest 1 week % increase :", inc_country, max_increase)
