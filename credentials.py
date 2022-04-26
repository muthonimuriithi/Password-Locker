class Credentials:
     '''
    class that creates instances of users accounts credentials
    '''

credentials_list = [] #creates an empty list for user credentials

def __init__(self, account_name, first_name, last_name, user_password):
        self.account_name = account_name
        self.first_name = first_name
        self.last_name = last_name
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
