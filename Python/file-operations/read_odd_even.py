file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\numbers.txt"

fr = open(file_path,"r")

# odd = [ num.rstrip("\n") for num in fr if int(num.rstrip("\n")) %2 != 0] 

# fr = open(file_path,"r")

# even = [ num.rstrip("\n") for num in fr if int(num.rstrip("\n")) %2 == 0] 



odd = []

even = []

for num in fr :

    num = num.rstrip("\n")

    if int(num)%2 == 0:

        even.append(num)

    else :

        odd.append(num)

print("odd numbers : ",odd)

print("even numbers : ",even)
