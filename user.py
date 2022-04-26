class User:
     '''
    class which creates instances of users
    '''

users_list = [] #creates an empty list for users


def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

def save_user(self):
        '''
        This method saves new object to users list
        '''
        User.users_list.append(self)

def delete_user(self):
            User.users_list.remove(self)