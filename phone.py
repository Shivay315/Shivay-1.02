while True:
    import os
    from contact import *
    from tabulate import tabulate
    import socket
    from tkinter import messagebox, Tk
    import time




    print(contact_list)

    h = ["NAME", "PHONE NUMBER 1","PHONE NUMBER 2"]
    print("""



    """)

    print(tabulate(contact_list, headers=h, tablefmt="psql"))

    print("""



    """)

    print("""
[1] To add contact number
[2] To edit any contact number
[0] To exit contact book
""")
    a = int(input("Enter here : "))


    if a == 1 :
        Name = input("Enter the name of person here : ")
        while True:
            PhoneNumber1 = input("Enter the 1st phone number here : ")
            if len(PhoneNumber1) == 10:
                PhoneNumber1 = int(PhoneNumber1)
                break
            else:
                print("You have entered wrong phone number(correct phone number has 10 digits) please enter again")
        while True:
            PhoneNumber2 = input("Enter the 2nd phone number here (If the person don't have 2nd phone number enter none) : ")
            
            if PhoneNumber2 == "None" or PhoneNumber2 == "none" or PhoneNumber2 == "NONE":
                contact_list.append([Name , PhoneNumber1 , PhoneNumber2])
                break

            else:
                
                if len(PhoneNumber2) == 10:
                    PhoneNumber2 = int(PhoneNumber2)
                    contact_list.append([Name , PhoneNumber1 , PhoneNumber2])
                    break
                else:
                    print("You have entered wrong phone number(correct phone number has 10 digits) please enter again")
    
    elif a == 2:
        s = True
        while s == True :
            print("To edit any contact number you have to first enter the name of the person.")
            edit_contact = input("Enter the name of the person here (Remember this is case-sensitive) : ")



            for i in range(0,len(contact_list)) :
                    if contact_list[i][0] == edit_contact:
                            break
                        
            print("The contact number you want to edit is", contact_list[i])
            print("If this is the contact you wanted to edit then enter 'y' else enter any other letter .")

            y_or_n = input("Enter here : ")

            if y_or_n == 'Y' or y_or_n == 'y':
                    s = False
                    new_name = input("Enter the new name here : ")
                    while True:
                        new_PhoneNumber1 = input("Enter the 1st phone number here : ")
                        if len(new_PhoneNumber1) == 10:
                            new_PhoneNumber1 = int(new_PhoneNumber1)
                            break
                        else:
                            print("You have entered wrong phone number(correct phone number has 10 digits) please enter again")
                    while True:
                        new_PhoneNumber2 = input("Enter the 2nd phone number here (If the person don't have 2nd phone number enter none) : ")

                        if new_PhoneNumber2 == "None" or new_PhoneNumber2 == "none" or new_PhoneNumber2 == "NONE":
                            contact_list[i] = [new_name , new_PhoneNumber1 , new_PhoneNumber2]
                            break
                        else:
                
                            if len(new_PhoneNumber2) == 10:
                                new_PhoneNumber2 = int(new_PhoneNumber2)
                                contact_list[i] = [new_name , new_PhoneNumber1 , new_PhoneNumber2]
                                break
                            else:
                                print("You have entered wrong phone number(correct phone number has 10 digits) please enter again")
    
    elif a == 0:
        os.system('exit')
        os.startfile('home.py')
        break
    print(contact_list)
    contact_list = str(contact_list)
    with open ('contact.py' , 'w') as f:
        f.write("contact_list = ")
    with open ('contact.py' , 'a') as f:
        f.write(contact_list)
    f.close()

    print("Task Ended")
print("BYE BYE")
