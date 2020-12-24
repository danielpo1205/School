## Lab focuses on Dictionary functions

info_dict1={"Dave":"30000","John":"20000","Hana":"35000","Rob":"90000","Magi":"15000"}

#Printing the sum of the first and last people
a=(int(info_dict1["Dave"]) + int(info_dict1["Magi"]))
print("Dave and Magi together have: " + str(a) + " NIS")

#Adding a person with the sum claculated above
info_dict1.update({"Debora":a})
print("The revised dictionary is: " + str(info_dict1))

#Checking the amount of entries in the dictionary
print("This dictionary has " + str(len(info_dict1)) + " entries")

#Does the name Idan listed in the dictionary?
print("idan" in info_dict1)
