#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

#user

def create_user(username, password):
    new_user = User(username, password)
    return new_user

def sv_user(user):
    user.sv_user()

def del_user(user):
        user.del_user()



def main():
    pass

if __name__ == '__main__':
    main()