file_path = "C:/Users/abhij/OneDrive/Desktop/development-journey-py/python-works/Tasks/Nov-27/students_data.csv"

fr = open(file_path,"r")

# read and print all rows

import csv

reader = csv.DictReader(fr)

data = [ row for row in reader ]

print(data)

# Count Total Students

total_students = len(data)

print("Total number of students : ",total_students)

# ⿣ Show Only Names
# Print only the Name column for all students.

names = [ stud.get("NAME") for stud in data ]

print("Names of all students : ",names)

# ⿤ Students in Python Batch
# Print all students whose BATCH = "Python".

python_students = [ stud.get("NAME") for stud in data if stud.get("BATCH ")=="Python" ]

print("Python students : ",python_students)

# ⿥ Students With 100% Attendance
# Print names of students whose PRESENT_% = 100.

present_100 = [ stud.get("NAME") for stud in data if stud.get("PRESENT_%")=="100" ]

print("Students With 100% Attendance : ",present_100)


# ⿦ Show MCQ1 Marks
# Print only names and MCQ1 values.

mcq1_marks = { stud.get("NAME") : stud.get("MCQ1") for stud in data }

print("Students with MCQ1 marks : ",mcq1_marks)



