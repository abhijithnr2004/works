file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\numbers.txt"

fr = open(file_path,"r")

rev = [ line.rstrip("\n")[::-1] for line in fr]


print(rev)