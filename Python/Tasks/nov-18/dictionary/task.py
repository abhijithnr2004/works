student = {"name": "Rahul", "age": 14, "grade": "B"}

print(student["name"])

student["school"] = "City High School"

print(student)

student["grade"] = "A+"

print(student)

student.pop("age")

print(student)

print(f"'name' exists : {"name" in student}")

print(len(student))

print("Keys : ",end="")
for key in student.keys():
    print(key,end=", ")

print("\nValues : ",end="")
for value in student.values():
    print(value,end=", ")

print("\nKey Value pair : ")
for key,value in student.items():
    print(f"{key} : {value}")