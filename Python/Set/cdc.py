str = "abcdcdbaabaa"

limit = len(str)+1

search_word = "aa"

count=0

for i in range(0,limit-len(search_word)) :
    if str[i:i+2] == search_word:
        count+=1

print(count)
