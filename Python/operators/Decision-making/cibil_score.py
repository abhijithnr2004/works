cibil_score = int(input("Enter cibil score : "))

if cibil_score in range(300,550) :
    print("poor")

elif cibil_score in range(550,650) :
    print("Average")

elif cibil_score in range(650,750) :
    print("good")

elif cibil_score in range(750,901) :
    print("Excellent")

else :
    print("Invalid input")