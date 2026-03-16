product = {"code" : 345 ,"title" : "Shirt" , "color" : "blue" ,"size" : "m","price" : 1500,"offer" : 200}

print(product["price"])

if "offer" in product :
    product["offer"]+=50

else :
    product["offer"] = 100

print(product)