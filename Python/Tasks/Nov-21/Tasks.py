# 11. print Mary's age

classroom = {
    "student1": {"name": "John", "age": 15},
    
    "student2": {"name": "Mary", "age": 16}
}

print("Age of Marie : ",classroom["student2"]["age"])



# 12. dictionary from two lists

keys = ["a","b","c"]

values = [1,2,3]

d = { keys[i] : values[i] for i in range(len(keys)) }

print(d)



# 1.1 print name of student 102

students = {
    "101" : {"name":"Rahul","age":14,"grade":"B"},
    
    "102" : {"name":"Anita","age":15,"grade":"A"}
}

print("Name of student 102 :",students["102"]["name"])



# 2. update Rahul grade

students["101"]["grade"] = "A+"



# 3. add new student

students["103"] = {"name":"Vikram","age":16,"grade":"B+"}



# 4. loop and print id → name

for sid, info in students.items() :
    
    print(sid, "->", info["name"])



# 5. access nested key

school = {
    "class10": {
        "teacher":"Mr. Kumar",
        
        "students":{"S1":"Ravi","S2":"Meena"}
    },
    
    "class9": {
        "teacher":"Mrs. Sharma",
        
        "students":{"S1":"Amit","S2":"Priya"}
    }
}

print(school["class9"]["teacher"])



# 6. employee directory

employees = {
    "E01":{"name":"Arjun","dept":"HR"},
    
    "E02":{"name":"Sara","dept":"IT"},
    
    "E03":{"name":"Manoj","dept":"Finance"}
}

print(employees["E02"]["dept"])



# 7. update Arjun dept

employees["E01"]["dept"] = "Admin"



# 8. add new employee

employees["E04"] = {"name":"Lakshmi","dept":"Marketing"}



# 9. print all employees

for eid, info in employees.items() :
    
    print(eid, "->", info["name"])



# 10. number of employees

print(len(employees))



# 11. cricket team

team = {
    "player1":{"name":"Rohit","role":"Batsman"},
    
    "player2":{"name":"Bumrah","role":"Bowler"}
}

print(team["player2"]["role"])



# 12. add matches for Rohit

team["player1"]["matches"] = 250



# 13. delete Bumrah role

del team["player2"]["role"]



# 14. deeply nested dictionary

company = {
    "sales":{"manager":"Kiran","team":{"T1":"Raj","T2":"Neha"}},
    
    "tech":{"manager":"Asha","team":{"T1":"Dev","T2":"Sonia"}}
}

print(company["tech"]["team"]["T2"])



# 15. print team member IDs from sales

print(company["sales"]["team"].keys())



# 16. student marks

marks = {
    "Rahul":{"math":85,"science":90},
    
    "Anita":{"math":78,"science":88}
}

print(marks["Anita"]["science"])
