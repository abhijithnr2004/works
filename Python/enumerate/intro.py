# lst = [1,2,3,4]

# for index,num in enumerate(lst,1) :

#     print(index+num,end = ",")

lst = [10,20,30,40]

dict_lst = { num : num**index for index,num in enumerate(lst,1) }

print(dict_lst)