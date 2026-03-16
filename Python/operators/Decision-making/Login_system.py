db_password = 1234

db_otp = 5000

password = int(input("Enter password : "))

if password == db_password :
    otp = int(input("Enter otp : "))

    if otp == db_otp :
        print("Login Success")

    else :
        print("Incorrect otp")

else :
    print("incorrect pin")

    