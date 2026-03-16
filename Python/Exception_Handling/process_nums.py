file_path = "Exception_Handling/nums.txt"

fr = open(file_path,"r")

all_nums = []

for line in fr :

    line.rstrip("\n")

    try :

        all_nums.append(int(line))

    except Exception as e :

        continue

even_nums = [num for num in all_nums if num%2==0 ]

print("even numbers : ",even_nums)

even_nums_count = {num : even_nums.count(num) for num in set(even_nums)}

print("even numbers count : ",even_nums_count)

max_even = {k for k,v in even_nums_count.items() if v==max(even_nums_count.values())}

print("most occured even number : ",max_even)



