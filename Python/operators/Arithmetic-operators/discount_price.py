price = int(input("Enter price : "))

discount = int(input("Enter discount in percentage : "))

final_price = price - ((price*discount)/100)

print("Final price : ",final_price)