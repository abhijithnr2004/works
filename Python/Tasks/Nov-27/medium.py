file_path = "C:/Users/abhij/OneDrive/Desktop/development-journey-py/python-works/Tasks/Nov-27/students_data.csv"

fr = open(file_path,"r")

import csv

reader = csv.DictReader(fr)

data = [ row for row in reader ]

# ⿡ Find Student With Highest OVERALL
# Print the name and OVERALL% of the top performer.

top_overall = [ float(stud.get("OVERALL")) for stud in data if stud.get("OVERALL").replace(".","").isdigit() ]

top_stud = { stud.get("NAME"):stud.get("OVERALL") for stud in data if stud.get("OVERALL")==str(max(top_overall))}

print("Student With Highest OVERALL : ",top_stud)


# ⿢ Filter LOW Performers (<30% Overall)
# Print students whose OVERALL < 30%.

low_performance = { stud.get("NAME") : stud.get("OVERALL") for stud in data if stud.get("OVERALL").replace(".","").isdigit() and float(stud.get("OVERALL"))<30 }

print("students whose OVERALL < 30% : ",low_performance)

# ⿣ Find Students With Missing Values(-)
# Print names of students who contain “-” in any column.

missing_values_students = [ stud.get("NAME") for stud in data if any(val == "-" for val in stud.values()) ]

print("names of students who contain “-” in any column : ",missing_values_students)

# ⿤ Append a New Student
# Add a new row to the existing CSV.

fw = open(file_path,"a")


# ⿥  Count Python vs Data Science Batch
# Print:
# Total Python students
# Total Data Science students
# ⿦ List Students With ABSENT_% > 20
# Print full details of students whose ABSENT_% > 20.
