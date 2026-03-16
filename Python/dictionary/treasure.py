treasure = {
    "box1" : "gold",
    "box2" : "silver",
    "box3" : "diamond",
    "box4" : "platinum"
}

print(treasure["box3"])

# adding new key value pair

treasure["box5"] = "iron"

# print(treasure)

#check and add new pair

if "box6" not in treasure :
    treasure["box6"] = "copper"
#     print(treasure)

# #iterating dictionary

# for k in treasure :

#     print(k,treasure[k])

# iterating only keys

# for k in treasure :

#     print(k)

# for k in treasure.keys() :
#     print("key = ",k)

# for v in treasure.values() :
#     print("values = ",v)

# for k,v in treasure.items() :
#     print(k,v)


print(treasure.get("box10","empty box"))

print("task1")

treasure.pop("box1")

print("treasure")
