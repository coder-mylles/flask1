

        

#         # check if saving multiple cridentials is possible .....................1
    def save_credentials(self):
        Credentials.credentials_list.append(self) 
        '''
        functions that saves credentials once defined
        '''   

    def create_credentials(account_name, login_detail , Password):

        new_credentials = Credentials(account_name, login_detail , Password)
        return new_credentials
            


#        # delete created credentials off our list
    def delete_credentials(self):        
        Credentials.credentials_list.remove(self) 
        '''
        used to delete credentials 
        '''

#     def    display_credentials(self):
#         Credentials.credentials_list.display(self)

         
#         #search for accounts
    @classmethod
    def find_account(cls, account_name):
        '''
        search for accounts
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials 

    
