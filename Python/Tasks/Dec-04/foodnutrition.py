file_path = "python-works/Tasks/Dec-04/Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

# print(data)




# fast foods

fast_foods = [ line.get("food_name") for line in data if line.get("category")=="Fast Foods" ]

print("fast foods :",fast_foods)



# Highest and lowest protien

food_protien = { line.get("food_name") : float(line.get("protein")) for line in data }

print(food_protien)

highest_protien = { k :v for k,v in food_protien.items() if v == max(food_protien.values()) }

print("Food with Highest protien : ",highest_protien)

lowest_protien = { k :v for k,v in food_protien.items() if v == min(food_protien.values()) }

print("Food with lowest protien : ",lowest_protien)




# total calorie  in each category

all_category = { line.get("category") for line in data}

all_calories = { }

for line in data :

    if line.get("category") in all_calories :

        all_calories[line.get("category")] += float(line.get("calories"))

    else :

        all_calories[line.get("category")] = float(line.get("calories"))

print(all_calories)





