file_path = "Exception_Handling\\numbers.txt"

try :
    fr = open(file_path,"r")

    numbers=[]

    try :

        for line in fr :

            line = line.strip("\n")

            try :

                numbers.append(int(line))

            

            except Exception as e :

                print("Error found : ",e)
    except :

        pass

    
    print(numbers)
    print("MAX : ",max(numbers))
    print("MIN : ",min(numbers))
    print("SUM : ",sum(numbers))

    num_count ={ num : numbers.count(num) for num in numbers }

    print(num_count)

    max_val = max(num_count.values())
    
    freq = [ k for k,v in num_count.items() if v==max_val]

    print("Highest frequent number : ",freq)


except Exception as e :

    print(e)



