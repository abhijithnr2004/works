words = ["cat","act","dam","mad","malayalam","madam"]

def palindrome_words(words) :

    p_words = []

    for w in words:

        if w == w[::-1] :
         p_words.append(w)

    return(p_words)

print(palindrome_words(words))



# palindrome_words = []

# for w in words :

#     if w == w[::-1] :
#         palindrome_words.append(w)

# print(palindrome_words)