#Practicing the "List" functions

#Creating a simple list containing personal info
details_list=['David Cohen','23','d@g.com','313-2124']
print("\nThe information recieved: " + "\nName: " + details_list[0] + "\nAge: " + details_list[1] + "\nE-mail address: " + details_list[2] + "\nPhone: " + details_list[3])

#Creating a list with 2 IP addresses
ip_list=['192.198.1.3', '10.100.5.21']
print("The 2 IP addresses are: " + str(ip_list))

#Adding two more IP addresses to the existing list
ip_list.append('20.5.13.47')
ip_list.append('16.51.80.2')
ip_list.append('10.10.1.1')
print("The updated IP list is: " + str(ip_list))

#Popping out the 3rd IP from the existing list
ip_list.pop(2)
print("The updated list of IP addresses without the 3rd column is: " + str(ip_list))
print("The number of IPs left in this list is:" + str(len(ip_list)))