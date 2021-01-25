# # Adding the contents of a single line in a *.*txt file to a list, placing each IP address in a single cell
# filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
# file = open(filename, "r")
# my_string = file.read()
# file.close()
# print(my_string)
# my_list = my_string.split(",")
# print(type(my_list))
# print(my_list)

# # Taking the contents of multiple lines in a *.*txt file and placing them in a list
# my_list = []
# filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
# file = open(filename, "r")
# for line in file:
#     print(line)
#     my_list.append(line)
# file.close()
# print(my_list)

# # Another option for adding multiple lines in a file to a list and then printing it to the screen - line by line
# filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
# file = open(filename, "r")
# new_list = (file.read().splitlines())
# print(type(new_list))
# print(new_list)
# file.close()
# for i in new_list:
#     print(i)

# Printing specific lines from a file
filename = "C:/Users/danie/Documents/סייבר ותכנות/Python/File_handling.txt"
file = open(filename, "r")
lines = file.readlines()
#lines = (file.readlines()[2])
print(lines[1])
print(lines[3])

# Creating a new *.*txt file
f = open("C:/Users/danie/Documents/סייבר ותכנות/Python/Test123.txt", "x")
f.close()
print("\nFile created")