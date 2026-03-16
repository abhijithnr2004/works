file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\words.txt"

fr = open(file_path,"r")

result = [ line.rstrip("\n").replace(" ","") for line in fr ]

# for line in fr :

#     line = line.replace(" ","")

#     # word = line.replace(" ","")

#     result.append(line.rstrip("\n"))

print(result)