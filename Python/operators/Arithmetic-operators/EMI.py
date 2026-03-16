Principal_amount = int(input("Enter the Principal amount : "))

Rate_of_interest = float(input("Enter the Rate of Interest per month : "))

number_of_months = int(input("Enter the number of Monthly installments : "))

# Convert percentage to decimal
Rate_of_interest = Rate_of_interest / 100

EMI = (Principal_amount*Rate_of_interest*(1+Rate_of_interest)**number_of_months)/((1+Rate_of_interest)**number_of_months-1)
                       
print("EMI Amount : ",round(EMI,2))                     