## Practicing file handling
# filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
# file = open(filename, "r")
# print(file.read())
# file.close()
#
# file = open(filename, "w")
# file.write("192.168.1.1\n192.168.1.2")
# file.close()

## Adding the "r+" permission
# filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
# file = open(filename, "r+")
# print(file.read())
# file.write("\n192.168.1.1\n192.168.1.2")
# print(file.read())
# file.close()
#
# # Appending a file (continuing the "r+" script)
# file = open(filename, "a")
# file.write("\n193.168.1.10\n193.168.1.11")
# file.close()
#
# # Printing the new output on the screen
# file = open(filename, "r")
# print(file.read())
# file.close()

## Adding a loop to print each line separately
filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
file = open(filename, "r")
for line in file:
    print(line)
file.close()
