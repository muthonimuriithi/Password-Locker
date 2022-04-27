import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):
        """
        Test class that defines test cases for the credential class behaviours
        """
        def setUp(self):
                """
                set up method to run before each test cases
                """
                self.new_credential = Credentials("twitter","loismuthons","poise")

        def tearDown(self):
                """
                tearDown method that does clean up after each test case has run
                """
                Credentials.credentials_list = []

        def test_init(self):
                """
                test_init test case to test if the object is initialized properly
                """
                
                self.assertEqual(self.new_credential.account_name,"twitter")
                self.assertEqual(self.new_credential.user_name,"loismuthons")
                self.assertEqual(self.new_credential.user_password,"poise")

        def test_save_credential(self):
                """
                test_save_credential test case to test if the credential object is saves into
                """
                self.new_credential.save_credentials()
                self.assertEqual(len(Credentials.credentials_list),1)

        def test_save_multiple_credentials(self):
                """
                test_save_multiple_credential to check if one can save multiple credentials
                """
                self.new_credential.save_credentials()
                test_credential = Credentials("twitter","loismuthons","poise")
                test_credential.save_credentials()
                self.assertEqual(len(Credentials.credentials_list),2)

        def test_delete_credential(self):
                '''
                test_delete_contact to test if we can remove credential from our credential list
                '''
                self.new_credential.save_credentials()
                test_credential = Credentials ("facebook","muthonslois","poison") # new credential
                test_credential.save_credentials()

                self.new_credential.delete_credential()# Deleting a credential object
                self.assertEqual(len(Credentials.credentials_list),1)   

        def test_display_all_credentials(self):
                """
                test_display_all_credentials to returns a list of all credentials saved
                """
                self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()