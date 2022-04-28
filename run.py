#!/usr/bin/env python3.8
import os
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

def create_credentials(account_name, user_name, user_password=None):
    if user_password is not None:
        new_credentials = Credentials(account_name, user_name, user_password)
    else:
        password=Credentials.genPassword()
        new_credentials = Credentials(account_name, user_name, password)
    return new_credentials

def s_credentials(credentials):
    credentials.save_credentials()

def del_credentials(account_name):
    credential= Credentials.search_credentials(account_name)

    credential.delete_credential()

def disp_credentials():
    credentials= Credentials.display_credentials()
    for credential in credentials:
        print(credential.account_name)
        print(credential.user_name)
        print(credential.user_password)

def search_creds(name):
    Credentials.search_credentials(name)

def login(name,password):
    return User.verify_user(name,password)
    

def show_codes():
    print(f"Please,Use these short codes to navigate the app:\ncc - create account, \nsc - show accounts,\ndc- delete account\n ex- exit")
    shortcode = input("Enter shortcode: ").lower().strip()
    return shortcode


def main():
        os.system("clear")
        print("Hey there! Welcome to password locker.")
        user_name = input("What is your username? ")
        user_password = input("Enter password: ")
        new_user=create_user(user_name, user_password)
        sv_user(new_user)
        print("You have been registered successfully. Please login.")
        login_username = input("Enter username: ")
        login_password = input("Enter password: ")
        login(login_username, login_password)
        print("Login successful.\n")
        os.system("clear")
        

        while True:
               

            shortcode = show_codes()
            if shortcode == "cc":
                account_name = input("Enter account name: ")
                account_username = input("Enter your username: ")
                pass_choice = input("Auto generate password? [y/N] ").lower().strip()

                if pass_choice == "n":
                    s_credentials( create_credentials(account_name, account_username))

                else :

                    password = input("Enter your password: ")
                    s_credentials( create_credentials(account_name, account_username, password ))
                    

            elif shortcode == "sc":
                disp_credentials()
                    

            elif shortcode == "dc":
                account_name = input ("Enter account name to delete: ")
                del_credentials(account_name)
        

            elif shortcode == "ex":
                print("Goodbye")
                                 

            else:print("I did not get that. Please enter the short codes")





              
        
if __name__ == '__main__':

    main()