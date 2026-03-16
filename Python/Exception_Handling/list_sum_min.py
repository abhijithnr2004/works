lst = ["10","20","hello","300","hai","4 00"]

num_lst = []

for num in lst :

    try :

        num_lst.append(int(num))

    except Exception as e :

        print(e)

print("SUM : ",sum(num_lst))
print("MIN : ",min(num_lst))
print("MAX : ",max(num_lst))
print("SORTED",sorted(num_lst))