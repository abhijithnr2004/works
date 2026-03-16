import csv

file_path = "Tasks/Nov-27/movies.csv"

fr = open(file_path, "r")

reader = csv.DictReader(fr)

data = [ row for row in reader ]


# read & display
for row in data[:5]:
    print(row)



# count lines
print(len(data))



# print column names
print(data[0].keys())



# filter by year
year = 2004

for row in data:
    if row["Year"] == year:
        print(row["Title"])



# highest rated movie
highest = 0
top_movie = ""

for row in data:
    if row["Rating"] != "":
        rating = float(row["Rating"])

        if rating > highest:
            highest = rating
            top_movie = row["Title"]

print(top_movie, highest)



# sort by rating
movies = [row for row in data if row["Rating"] != ""]

sorted_movies = sorted(movies, key=lambda x: float(x["Rating"]), reverse=True)

with open("sorted_movies.csv", "w", newline="") as f:

    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()

    for row in sorted_movies:
        writer.writerow(row)



# find movies with missing data
for row in data:
    if "" in row.values():
        print(row)



# average runtime
total = 0
count = 0

for row in data:
    if row["Runtime"].isdigit():
        total += int(row["Runtime"])
        count += 1

print(round(total / count, 2))
