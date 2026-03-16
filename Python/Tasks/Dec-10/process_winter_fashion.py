import csv

file_path = "python-works\Tasks\Dec-10\Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

reader = csv.DictReader(fr)

data = [row for row in reader]

# all brands

brands = { line.get("Brand") for line in data }

print("All brands : ",brands)

# price > 750

print("Price > 750 :")

for line in data :

    price = float(line.get("Price(USD)"))

    if price > 750 :

        print(line.get("Brand"), line.get("Category"), price)

# count per category

category_count = {}

for line in data :

    cat = line.get("Category")

    if cat in category_count :

        category_count[cat] += 1

    else :

        category_count[cat] = 1

print("Count per category : ",category_count)

# Trending with greater than 4.5 rating

for line in data :

    if line.get("Trend_Status") == "Trending" :

        rating = float(line.get("Customer_Rating"))

        if rating > 4.5 :

            print(line.get("Brand"), line.get("Category"), rating)

# most expensive product

max_price = 0

exp_item = None

for line in data :

    price = float(line.get("Price(USD)"))

    if price > max_price :

        max_price = price

        exp_item = line

print(f"Most expensive product : {exp_item.get("Material")}, Brand: {exp_item.get("Brand")}, category : {exp_item.get("Category")}, price : {max_price}")