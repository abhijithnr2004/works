file_path = "python-works\Exception_Handling\cart\cart_items_100.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

order_summary = {}

for order in data:

    title = order.get("title")

    qty = int(order.get("quantity",0))

    if title in order_summary :

        order_summary[title]+=qty
    
    else :

        order_summary[title]=qty

print(order_summary)

all_users = [order.get("user") for order in data]

user_count = {user : all_users.count(user) for user in set(all_users)}

print("count of orders by users : ",user_count)

max_user = {k for k,v in user_count.items() if v==max(user_count.values())}

print("most ordered user : ",max_user)


