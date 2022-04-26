import pyperclip
import unittest

from credentials import Credentials
class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method that runs before each Test
        '''
        self.new_credentials = Credentials("twitter","billowbashir","123456789")
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list=[]
    def test_init(self):
        self.assertEqual(self.new_credentials.platform_name,"twitter")
        self.assertEqual(self.new_credentials.username,"billowbashir")
        self.assertEqual(self.new_credentials.password,"123456789")
    def test_save_credentials(self):
        '''
        test case to test if the object is saved into the credentials_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_save_multiple_credentials(self):
        '''
        test case to test if we can save multiple credentials into the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("test","testname","987654321")
        test_credentials.save_credentials()

        self.assertEqual(len(Credentials.credentials_list),2)
    def test_delete_credentials(self):
        '''
        test case to test if we can delete credentials from the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("test","testname","987654321")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_credentials_by_platform_name(self):
        '''
        test case to test if we can search for credentials in the credentials_list by the platform_name and display
        '''
        test_credentials = Credentials("test","testname","987654321")
        test_credentials.save_credentials()

        found_credential=Credentials.find_credentials_by_platform_name("test")
        self.assertEqual(found_credential.username,test_credentials.username)
    def test_credentials_exists(self):
        '''
        test case to test whether we can return a boolean value if we cannot find the credentials we search for
        '''
        test_credentials = Credentials("test","testname","987654321")
        test_credentials.save_credentials()
        credentials_exists= Credentials.credentials_exists("test")

        self.assertTrue(credentials_exists)
    def test_display_all_credentials(self):
        '''
        test case to test whether we can display a list of all save credentials
        '''
        self.assertEqual(Credentials.display_all_credentials(),Credentials.credentials_list)
    # def test_copy_password(self):
    #     '''
    #     test case to test we can copy the password to machine clipboard
    #     '''
    #     self.new_credentials.save_credentials()
    #     Credentials.copy_password("twitter")
    #
    #     self.assertEqual(self.new_credentials.platform_name,pyperclip.paste())




if __name__ =='__main__':
    unittest.main()