# Importing supporting functions to run on the main code in "FinalLab_main"
from time import sleep
import re
import os

# Creating a dictionary for the DNS.
dns_dict = {}

# Program's main Menu:
def menu():
    choice = input('''
        Main menu - Please choose one of the following:
        A. IP system - administrator's menu.
        B. DNS system - administrator's menu.
        ''')

    # Sub-menu:
    if choice == "A" or choice == "a":
        sleep(2)
        sub_choice = input('''
            IP system:
            1. Search for an IP address in the database.
            2. Add an IP address to the database.
            3. Delete an IP address from the database.
            4. Print to the screen all the IPs currently stored on file.
            ''')
        sleep(2)

        if sub_choice == "1":
            search_ip()

        elif sub_choice == "2":
            add_ip()

        elif sub_choice == "3":
            del_ip()

        elif sub_choice == "4":
            print_ip()

    elif choice == "B" or choice == "b":
        sleep(2)
        sub_choice = input('''
            DNS system:
            1. Search for a URL in the DNS dictionary.
            2. Add a URL + IP address to the dictionary.
            3. Delete a URL from the dictionary.
            4. Update the IP address of a specific URL.
            5. Print to the screen all URL:IP entries in the dictionary.
            ''')
        sleep(2)

        if sub_choice == "1":
            search_url()

        elif sub_choice == "2":
            add_url()

        elif sub_choice == "3":
            del_url()

        elif sub_choice == "4":
            update_url()

        elif sub_choice == "5":
            print_url()

    else:
        sleep(2)
        print("\nThe option you have entered is incorrect. Please choose between A or B.")

# The functions for operating the sub menus:
def search_ip():
    ipadrs = input("\nPlease type in an IP address: ")
    sleep(2)
    print("Please wait while the system is searching for IP address: " + ipadrs)
    sleep(2)
    file = open("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt", "r")
    fi = file.readlines()
    re_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})')
    for line in fi:
        ip = re.findall(re_ip, line)
        if ipadrs in line:
            sleep(2)
            print("IP " + str(ipadrs) + " was found in the database.")
        else:
            if os.stat("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt").st_size == 0:
                sleep(2)
                print("IP " + str(ipadrs) + " couldn't be found.")
            else:
                sleep(2)
                print("IP " + str(ipadrs) + " couldn't be found.")
    file.close()

def add_ip():
    ipadrs = input("\nPlease type in an IP address: ")
    sleep(3)
    file = open("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt", "a")
    file.write(ipadrs)
    file.close()
    sleep(1)
    print("IP address " + str(ipadrs) + " was successfully added to the list.")

def del_ip():
    ipadrs = input("\nPlease type in an IP address to remove from database: ")
    sleep(3)
    with open("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt", "r") as file:
        lines = file.readlines()
    with open("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != (ipadrs):
                file.write(line)
    sleep(2)
    print("IP address " + str(ipadrs) + " was successfully removed from the list.")

def print_ip():
    with open("C:/Users/danie/Documents/לימודים/אבטחת סייבר/Python/IP_database.txt", "r") as file:
        data = file.read()
        print("The database contains the following IP address:\n" + data)

def search_url():
    key = input("\nWhat is the URL address you wish to search for? ")
    sleep(2)
    if (key in dns_dict):
        print("The URL - " + key + " was found in the dictionary.")
    else:
        print("The URL " + key + " was not found.")

def add_url():
    key = input("\nPlease enter the URL address to be added to the DNS system: ")
    value = input("Now, type in the IP address for the URL '" + key + "':")
    dns_dict.update({key: value})
    sleep(2)
    print("\nThe URL " + key + " and IP address " + value + " were added to the system.\n")
    sleep(1)
    print(dns_dict)

def del_url():
    print("The DNS currently contains the following addresses:")
    print(dns_dict)
    sleep(2)
    key = input("\nPlease enter the URL address to be removed from the DNS: ")
    dns_dict.pop(key, None)
    sleep(2)
    print("\nThe URL " + key + " was successfully removed from the DNS system.")

def update_url():
    key = input("What is the URL of the IP address you wish to change? ")
    sleep(1)
    newval = input("What is the new IP address for this URL? ")
    sleep(2)
    dns_dict[key] = newval
    sleep(2)
    print("The IP address for URL " + key + " was successfully updated to: " + newval)
    sleep(1)
    print(dns_dict)

def print_url():
    print("The DNS currently contains the following addresses:")
    print(dns_dict)