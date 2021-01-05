# Practicing functions
#
# def my_function():
#     print("Hello function")
#
# my_function()
#
# my_function()

##############################

# def my_function(name):
#     print(name + '.net')
#
# my_function("dog")
# my_function("bog")
# my_function("zog")

##############################

# def my_function(x):
#      return x*x
#
# print(my_function(3))
# print(my_function(2))

##############################
#
# def my_function(name="dor"):
#     print(name + '.net')
#
# my_function("boss")
# my_function()

###############################

#
# def my_function(service, name="dor"):
#     print(service + ':' + name + '.net')
#
# my_function("ping","boss")
# my_function("ssh")

###############################

# Example:

def add_ip(list,ip1,ip2,ip3):
    print("List inside def: " + str(list))
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list

ip_list=[]
ip_n1=input("Enter first IP: ")
ip_n2=input("Enter 2nd IP: ")
ip_n3=input("Enter 3rd IP: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
#ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)
