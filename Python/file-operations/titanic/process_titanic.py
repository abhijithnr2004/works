file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\titanic\\Titanic-Dataset.csv"

fr = open(file_path,"r")

# row = fr.readline()

# print(row)

# for line in fr :

#     lst = line.rstrip("\n").split(",")

#     id = lst[0]
#     survived = lst[1]
#     pclass = lst[2]
#     name = lst[3].lstrip('"')
#     sex = lst[5]
#     age = lst[6]
#     sibsp = lst[7]
#     parch = lst[8]
#     fare = lst[10]
#     cabin = lst[11]
#     embarked = lst[12]

#     lst = []

    # print(name,age)

import csv

reader = csv.DictReader(fr)

data = [ row for row in reader ]

# print(data)

# name = [ line.get("Name") for line in data ]

# for n in name :

#     print(n)

# genders = [ line.get("Sex") for line in data ]

# male_count = genders.count("male")

# female_count = genders.count("female")

# print("male count : ",male_count)
# print("female count : ",female_count)

# survived = [ line.get("Survived") for line in data ]

# survived_count = survived.count("1")

# print("Count of survived : ",survived_count)

class_count = [ p.get("Pclass") for p in data]

# print("class 1 count : ",class_count.count("1"))
# print("class 2 count : ",class_count.count("2"))
# print("class 3 count : ",class_count.count("3"))

# youngest and oldest 

age_list = [ int(p.get("Age")) for p in data if p.get("Age").isdigit()]


youngest = {p.get("Name") : p.get("Age") for p in data if p.get("Age") == str(min(age_list))}
oldest = {p.get("Name") : p.get("Age") for p in data if p.get("Age") == str(max(age_list))}

# print("youngest : ",youngest)

# print("oldest : ",oldest)

# get names of first 10 passengers

first_ten = data[:11]

first_ten_names = [p.get("Name") for p in first_ten]

# print("First 10 passengers : ",first_ten_names)

# count of passengers from each port

all_passengers_boarding_station = [ p.get("Embarked") for p in data if len(p.get("Embarked"))>0 ]

boarding_count = { s:all_passengers_boarding_station.count(s) for s in all_passengers_boarding_station }

# print("count of passengers from each port : ",boarding_count)

#count of children(<10)

children_count = [ p for p in data if p.get("Age").isdigit() and int(p.get("Age"))<10 ]

print("count of children : ",len(children_count))

survived_children_count = [ p for p in children_count  if p.get("Survived")=="1" ]

print("count of survived children : ",len(survived_children_count))

# survival ratio

total_count = [ line.get("Survived") for line in data ]

survived_count = total_count.count("1")

survived_ratio = (survived_count/len(total_count)) * 100

print("survived passenger rate : ",round(survived_ratio,2))

# survival rate of each gender

genders = [ line.get("Sex") for line in data ]



male_count = genders.count("male")

female_count = genders.count("female")

survived_males = [ p for p in data if p.get("Survived")=="1" and p.get("Sex")=="male" ]

survived_males_count = len(survived_males)

survived_females = [ p for p in data if p.get("Survived")=="1" and p.get("Sex")=="female" ]

survived_females_count = len(survived_females)

survived_males_ratio = (survived_males_count/male_count) * 100

survived_females_ratio = (survived_females_count/female_count) * 100

print("survived male ratio : ",round(survived_males_ratio,2))

print("survived female ratio : ",round(survived_females_ratio,2))


# class wise survival ratio

all_pass_class = [p.get("Pclass") for p in data]

total_class_count = { c:all_pass_class.count(c) for c in all_pass_class }

# print(total_class_count)

all_pass_survived_class = [p.get("Pclass") for p in data if p.get("Survived")=="1"]

class_survival_count = { c : all_pass_survived_class.count(c) for c in all_pass_class}

# print(class_survival_count)

class_survival_rate = { c : round(((all_pass_survived_class.count(c)/all_pass_class.count(c))*100),2) for c in all_pass_class}

print("survival ratio in each class :",class_survival_rate)