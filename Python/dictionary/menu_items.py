menu_items = {
    "idli" : 12,
    "dosa" : 10,
    "egg curry" : 30,
    "fish fry"  : 40,
    "chicken" : 80,
    "Beef" : 100
}

print(menu_items)

for k in menu_items.keys() :
    print(k)

for k,v in menu_items.items() :
    print(k,v)

for k,v in menu_items.items() :
    if v<50 :
        print(k)

item_price=menu_items.get("sambar",0) 
print(item_price)

#check and update

if "egg curry" in menu_items :
    menu_items["egg curry"] += 15

print(menu_items)