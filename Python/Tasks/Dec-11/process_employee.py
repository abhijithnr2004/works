import csv

file_path = "python-works\Tasks\Dec-11\employee_salary_dataset.csv"

fr = open(file_path, "r", encoding="utf-8")

reader = csv.DictReader(fr)

data = [row for row in reader]


# employee with highest salary
max_salary = 0
max_emp = ""

for emp in data:
    salary = int(emp["Monthly_Salary"])
    if salary > max_salary:
        max_salary = salary
        max_emp = emp["Name"]

print("employee with highest salary : ",max_emp, max_salary)


# average salary
total = 0
for emp in data:
    total += int(emp["Monthly_Salary"])

print("average salary :",total / len(data))


# count employees by department
dept_count = {}

print("count employees by department : ")

for emp in data:
    dept = emp["Department"]
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1

for d in dept_count:
    print(d, dept_count[d])


# employees with salary > 100000
print("employees with salary > 100000 : ")
for emp in data:
    if int(emp["Monthly_Salary"]) > 100000:
        print(emp["Name"], emp["Monthly_Salary"],end= ",")


