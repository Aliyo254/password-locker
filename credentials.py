class Credentials:
    '''
    class that generates new instance of the credential details
    '''
    credentials_list = []
    def __init__(self,platform_name,username,password):
        self.platform_name=platform_name
        self.username=username
        self.password=password


    def save_credentials(self):
        '''
        method to save credentials to credentials_list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        method to delete credentials from credentials_list
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_credentials_by_platform_name(cls,platform_name):
        '''
        method to search through the credentials_listby platform name and return the credentials
        '''
        for credential in cls.credentials_list:
            if credential.platform_name == platform_name:
                return credential
    @classmethod
    def credentials_exists(cls,platform_name):
        '''
        method that  searches through the credentials_list by platform_name to check whether a credential exist and returns a boolean value
        '''
        for credential in cls.credentials_list:
            if credential.platform_name==platform_name:
                return True
            return False
    @classmethod
    def  display_all_credentials(cls):
        '''
        method to display list of saved credentials
        '''
        return cls.credentials_list
    # @classmethod
    # def copy_password(cls,platform_name):
    #     credentials_found = Credentials.find_credentials_by_platform_name(platform_name)
    #     pyperclip.copy(credentials_found.password)
