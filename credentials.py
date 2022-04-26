from random import randint
from user import User

class Credentials:
     '''
    class that creates instances of users accounts credentials
    '''

credentials_list = [] #creates an empty list for user credentials

def __init__(self, account_name, user_name, user_password):
        self.account_name = account_name
        self.user_name = user_name
        self.user_password = user_password

def save_credential(self):
        '''
        Method to save a new object in the credential list
        '''
        Credentials.credentials_list.append(self)

def delete_credentials(self):
        '''
        Method to remove a credential from the credential list
        '''
        Credentials.credentials_list.remove(self)


@classmethod
def display_credentials(cls):
        '''
        Method that displays the credentials list
        '''
        return cls.credentials_list

@classmethod
def verify_user(cls,user_name, user_password):
    active_user = " "
    for user in User.users_list:
        if(user.username == user_name and user.password == user_password):
            active_user = user.username

            return active_user


@classmethod
def search_credentials(cls, account_name):
    for credential in cls.credentials_list:
        if credential.account_name == account_name:
            return credential

def generate_password(ln):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!#-$*/=?@"
    password =" "
    for i in range(ln):
        password += chars[randint(0, len(chars)-1)]
        return password
