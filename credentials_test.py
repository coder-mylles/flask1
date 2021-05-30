import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test Class to test the behaviour of the credentials class
    '''
    def setUp(self):    
        self.new_credentials = Credentials("Facebook", "0712345678", "alfiecode")
    

   # The tearDown() method allows us to clean up.
   # def tearDown(self):
   # Credentials.credentials_list = []

    def test_init(self):
        
            self.assertEqual(self.new_credentials.account_name, "Facebook",)
            self.assertEqual(self.new_credentials.login_detail, "0712345678")
            self.assertEqual(self.new_credentials.Password, "alfiecode")
            '''
            confirms that initialisation of class Credentials happens as expected.Three parameters etc
            '''
    
   

if __name__ == "__main__":
    unittest.main()
