#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

#user

def create_user(user_name, user_password):
    new_user = User(user_name, user_password)
    return new_user

def sv_user(user):
    user.save_user()

def del_user(user):
        user.delete_user()

        #objects in credentials classmethod

def create_credentials(account_name, user_name, user_password):
    new_credentials = Credentials(account_name, user_name, user_password)
    return new_credentials

def s_credentials(credentials):
    credentials.save_credentials()

def del_credentials(credentials):
    credentials.delete_credentials()

def disp_credentials():
    return Credentials.display_credentials()

def search_creds(name):
    Credentials.search_credentials(name)

def login(name,password):
    return Credentials.verify_user(name,password)



def main():
        print("Hey there! Welcome to password . What is your name? ")
        user_name = input("Name:")

        while True:
            print(f"Hey {user_name} ,Use these short codes to enter your options:\ncc - create account, \nli - login,\n ex- exit")
            shortcode = input().lower().strip()
            if shortcode == "cc":
                print("Enter the user details")
                print("-"*10)
                user_name = input("username: ")

                while True:
                    print("Enter: ip-to input password\n  gp- to generate password ")
                    pass_choice = input("choice: ").lower().strip()

                    if pass_choice== "ip":
                        password = input("Enter your password\n")
                    elif pass_choice== "gp":
                        password = Credentials.generate_password(8)
                    else:
                            print("Invalid. kindly use short codes")

                            sv_user(create_user(user_name, user_password))

            elif shortcode == "li":
                print("Enter your login details")
                user_name = input("user-name: ")
                user_password = input("Password: ")

                user_exist = login(user_name, user_password)

                if user_exist == user_name:
                    
                    print("Welcome {user_name}")

                while True:
                    print("Use these short codes to navigate : cc- create new account dc- display credentials f- find credentials ex- exit")

                    shortcode = input().lower().strip()
                    if shortcode == "cc":
                        print("Enter details to create new account")
                        a_name = input("Account Name: ")
                        u_name = input("Username: ")

                        while True:
                            print("Enter ip-to input password\n gp- to generate password ")
                            pass_choice = input("choice: ").lower().strip()

                    if pass_choice== "ip":
                        password = input("Enter your password\n")
                    elif pass_choice== "gp":
                        password = Credentials.genPassword(8)
                    else:
                            print("Invalid. kindly use short codes")

                    s_credentials(create_credentials(a_name,u_name,password))
                    print(f"{a_name} account of username {u_name} and password")

            elif shortcode == "dc":
                        if disp_credentials():
                            print(f"Account{Credentials.account_name} -- {Credentials.username} -- password{password}")

            else: 
                print("There are no saved credentials yet")

                # elif shortcode == "ex":
                #     print("Goodbye")
                #              break

                # else:print("I did not get that. Please enter the short codes")





            # elif shortcode == "ex":
            #     print("Goodbye")
            
if __name__ == '__main__':
    
    main()