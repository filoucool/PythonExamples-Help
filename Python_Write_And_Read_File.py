#WRITE
filename = "YourFileName.txt"
fileHandler = open(filename, "w")
fileHandler.write("ADD YOUR TEXT HERE")
# Use \n for a new line
fileHandler.close()

#READ
fileHandler = open(filename, "r")
for line in fileHandler:
  print(line)
fileHandler.close()