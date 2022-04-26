import unittest

import pyperclip
class User:
    user_list=[]
    def __init__(self,name,username,email,password):
        self.name=name
        self.username=username
        self.password=password
        self.email=email

    def save_user(self):
         '''
         method to save user login DETAILS
         '''
         User.user_list.append(self)
    
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in username and returns a user that matches the username
        
        Args:
            username: User's name to search for
            
        Returns:
            User that matches the username
        '''
        
        for user in cls.user_list:
            if user.username == username:
                return user
                

    @classmethod
    def copy_email(cls,username):
        user_found = User.find_by_username(username)
        pyperclip.copy(user_found.email)
    