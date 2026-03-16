weight_in_kg = int(input("Enter weight in kg : "))

height_in_cm = int(input("Enter heightt in cm : "))

height_in_meter = height_in_cm/100

bmi = weight_in_kg/(height_in_meter**2)

print(round(bmi,0))

if bmi >= 30 :
    print("Obese")

elif bmi >= 25 :
    print("Overweight")

elif bmi >= 20 :
    print("Normal weight")

elif bmi < 20 :
    print("Underweight")

else :
    print("Invalid input")