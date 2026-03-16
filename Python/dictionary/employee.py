employee = { "id" : 11 , "name" : "Abhi","department" : "sales", "location" : "Thrissur","salary" : 10000}

print(employee["name"])

#add new 
employee["email"] = "Abhi@gmail.com" #add new key-value pair if key doesnt exist else update value of existing key

print(employee["email"])

employee["salary"] = 15000  # updates value of salary

print(employee["salary"])

# Cheking if key exist

if "salary" in employee : #passes key 
    print("exist")
else :
    print("not exist")