
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
    
    #check if our credentials can be saved............2
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        '''
        confirms if cridentials can be saved
        '''


    #   check if users can store multiple credentials..................3
    def test_saving_multiple_creds(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),4)
        '''
        Checks if saving multiple credentials is possible
        '''

    #  test if you can delete credentials test ...............4
    def test_delete_credentials(self): 
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    #   # to test if credentials are searchable..................5
    # def test_search_for_credentials(self):  
    #     self.new_credentials.save_credentials()
    #     test_credentials = Credentials("Instagram", "bigman@gmail.com","Sociallife01")
    #     test_credentials.save_credentials()
    #     find_credentials= Credentials.find_account("Instagram")
    #     self.assertEqual(find_credentials.account_name, test_credentials.account )

       

if __name__ == "__main__":
    unittest.main()
