#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
# import pyperclip
import string
import random
from pyfiglet import Figlet

# 1. function to create new user
def create_user( user_name, email, password):
	'''
	function to create new user
	'''
	new_user = User(user_name, email, password)
	return new_user

#  2. Function that saves User
def save_user(self):
	'''
	Method that saves User
	'''
	User.save_user("self")


#    3. Function that deletes user
def delete_user(self):
	'''
	Function that deletes user
	'''
	User.delete_user()

        # 4. Function that finds user when one choses to log in.
def find_user(email, password):
	'''
	Function that finds user when one choses to log in.
	'''
	return  User.find_user(email, password)

    # 5. Function that checks for existing Users
# def check_existing_user(user):
'''
Function that checks for existing Users
'''
#     return User.check_existing_user(user)

    #6. function that saves Users
def display_users():
	'''
	function that saves Users
	'''
	return User.display_users()

# def new_credentials(account_name, login_detail , Password):
# 	new_credentials(save_credentials)

def create_credentials(account_name, login_detail , Password):

    new_credentials = Credentials(account_name, login_detail , Password)
    return new_credentials
        




def save_credentials():
	'''
	methods that saves credentials.
	'''
	return Credentials.save_credentials()

	#7. Function that copies cridentials on clipboard

def create_credentials( save_credentials):
	'''
	function to create new user
	'''
	Credentials.create_credentials("account_name", "login_detail" , "Password")
	

def copy_User_credential():
	'''
	Function that copies cridentials on clipboard
	'''
	return User.find_user(email)
# pyperclip.copy(user_found.email)

def passGen(size = 8, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    gen = ''.join(random.choice(char) for _ in range(size))
    return gen



def main():

	# custom_fig = Figlet(font='speed')
	# print(custom_fig.renderText('PASSWORD SAFE'))

	print("Welcome to Password Safe.Follow through our Menu and enter the shortcode to navigate:\n sign ---- to sign up,\n log ----   to log In,\n  exit ---- to exit ")
	
	
	print("*" *80)
	
	code = input().lower()
	# .........................trial.........................
	if code == "log":  #create the log in logic if user already has an account
			
		print("Enter your  Username")
		user_name = input().lower()

		# print("Enter your email adress")
		# email = input().lower()

		print ("Enter your password")
		password = input()
		
		if find_user(user_name, password) == password:  #can take user_name as the third parameter
			print("Successfully logged in")	
	

		else:
			print("Your cridentials don't match any account.Enter the shortcode sign, to Sign up and access Application.")
			
			code = input()

# ................................trial........................
	elif code == "sign":
		print("Enter your details to create account")
		print("Enter Username")
		user_name = input().lower()

		print("Enter your email adress")
		email = input().lower()

		print("Enter your password")
		password = input()
		save_user(create_user( user_name, email, password))
		# save_user( user_name, password)

		print(f"Welcome {user_name} to Password Safe.You are now logged in.")
		print("\n")
			# Accessible to Users who have already logged in Only
		print("Use the following shortcodes to proceed :\n create - create new account details,\n display - display accounts,\n find - find an account,\n exit - exit the Application")
		while True:
			code = input()
			if code == "create":
				print("Please enter the Account details for the password you want to save: ")
				print("Account name")
				account = input()
				print("LogIn cridential used.eg. phone number,email ")
				email = input()
				print ("Enter 1 to input a password, to have one automatically generated for you enter 2.")
				
				password_choice = input()

				
				if password_choice == "1":
					password = print(input("enter your password"))
					print(password)
					
				
				elif password_choice == "2":
					password = passGen()
					print(password)

				
				else:
					print("Please input shortcode 1 or 2.")
					
					
				# save_credentials(create_credentials)
				create_credentials( save_credentials)

				print(f"You have successfully added an account with the following details\nAccount name: {account}\nLog in cridential used: {email}\nPassword: {password}.")
				print("To create another account type in create,to display accounts created type display,to exit type exit")
				
			elif code == "display":

				save_user(create_user(user_name, email, password)) # create and save new password.

				print ("\n")
				print(f"A new user,with a user name {user_name} and email {email} has been added")
				
				print("Dear User,please use the given shortcodes to proceed")




	# elif code == "log":  #create the log in logic if user already has an account
			
	# 	print("Enter your  Username")
	# 	user_name = input().lower()

	# 	# print("Enter your email adress")
	# 	# email = input().lower()

	# 	print ("Enter your password")
	# 	password = input()
		
	# 	if find_user(user_name, password) == password:  #can take user_name as the third parameter
	# 		print("Successfully logged in")	
	

	# 	while True:
	# 		print("Your cridentials don't match any account.Enter the shortcode sign, to Sign up and access Application.")
	# 		code = input()
		
		
	elif code =="exit":
		print("Logging Out ... .  .   .    .     .      .         .       .")

		print("\n")	
		print("Adios,Have a nice time!")




	else:
		print("Dear User,you have entered an invalid shortcode.Please enter the following short codes to access Password Safe:\n sign - Sign Up,")


if __name__ == '__main__':
    main()  

        
