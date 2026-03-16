file_path = "C:\\Users\\abhij\\OneDrive\\Desktop\\development-journey-py\\python-works\\file-operations\\greetings.txt"

fr = open(file_path,"r")

st = { line.rstrip("\n") for line in fr }

print(st)