# Zero Division error

num1 = int(input("Enter number 1 : "))

num2 = int(input("Enter second number : "))

try :

    result = num1/num2

    print (result)

except Exception as e :
    print(e)

print("file operations")

# FileNotFound error

file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\abc.txt"

try :

    fr = open(file_path,"r")

    for line in fr :

        print(line)

except Exception as e :

    print(e)


print("Database commit")
