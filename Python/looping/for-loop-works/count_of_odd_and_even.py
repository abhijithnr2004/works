num = int(input("Enter limit : "))

odd = 0
even = 0

for i in range (1,num+1):
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print("Count of odd : ",odd)
print("Count of even : ",even)