import unittest
from user import User
class TestUser(unittest.TestCase):

    '''
    Test class that defines test  for the User class behaviours.
    '''

    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''
 
        self.new_user = User("Ndundiro", "ndundirokamau@gmail.com", "Kamau") 

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []
        # User.user_list = []

        def test_init(self):

            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_user.user_name,"Ndundiro")
            self.assertEqual(self.new_user.email,"ndundirokamau@gmail.com") #Check how initialisation happens as expected.
            self.assertEqual(self.new_user.password,"12345abc")




    def test_save_user(self):
        '''
            test case to test if new user  is saved into the contact list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

 
        #check whether you can store more than one user..............2
    
    def test_save_mutliple_users(self):
        '''
        test case to see if we can save multiple users.
        '''
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

        # Test if a user can be deleted from our account .........3

    def test_delete_user(self):
        '''
        test case to see if we can delete a user
        '''
        self.new_user.save_user()
        test_user = User("username", "email", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

        #find a user using username ....................4
    # def test_find_user(self):
    #     '''
    #     find a user using their username
    #     '''
    #     self.new_user.save_user()
    #     test_user = User("user_name", "email", "password")
    #     test_user.save_user()
    #     self.find_user.test_user("email", "12345abc")  
    #     self.assertEqual(find_user.email, new_user.email)




if __name__ == "__main__":
    unittest.main()

  