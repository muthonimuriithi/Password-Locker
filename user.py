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

                #from here

        @classmethod
        def find_by_user_name(cls,user_name):
                '''
                Method that takes in a user_name and returns a user that matches that user.
                Args:
                user_name: user_name to search for
                Returns :
                user of person that matches the number.
                '''

                for user in cls.users_list:
                        if user.user_name == user_name:
                                return user

        @classmethod
        def user_exist(cls,user_name):
                '''
                Method that checks if a user exists from the user list.
                Args:
                user_name: user_name to search for
                Boolean: True or false depending if the user exists
                '''
                for user in cls.users_list:
                        if user.user_name == user_name:
                                return True


        def delete_user(self):
         User.users_list.remove(self)