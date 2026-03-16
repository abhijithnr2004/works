db_pin = 1234

db_balance = 5000

pin = int(input("Enter PIN : "))

if pin == db_pin :
    amount = int(input("Enter amount : "))

    if amount < db_balance :
        print("Success")
    
    else :
        print("Insufficient Balance")

else:
    print("Incorrect pin")
