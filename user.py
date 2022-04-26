import unittest
class User:
    user_list=[]
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password

    def save_user(self):
         '''
         method to save user login DETAILS
         '''
         User.user_list.append(self)