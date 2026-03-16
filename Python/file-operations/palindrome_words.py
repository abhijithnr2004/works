file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\words.txt"

fr = open(file_path,"r")

space_removed = [ line.rstrip("\n").replace(" ","") for line in fr ]

# print(space_removed)

palindrome_words = [ words for words in space_removed  if words[::-1]==words ]

print("palindrome words : ",palindrome_words)