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
            Credentials.display_credentials()



def main():
    pass

if __name__ == '__main__':
    main()