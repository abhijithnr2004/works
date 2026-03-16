
Principal_amount = int(input("Enter the Principal amount: "))

Rate_of_interest = float(input("Enter the Rate of Interest: "))

Tenure = int(input("Enter the Time (in years): "))

Simple_interest = (Principal_amount * Rate_of_interest * Tenure) / 100

print("Simple Interest:", round(Simple_interest, 2))
