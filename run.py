#!/usr/bin/env python3.6
from myAccounts import Accounts
import string, random 

def add_account(account,usr_name,a_password):
  '''
  Function to add new account details
  '''
  new_myaccounts = Accounts(account,usr_name,a_password)
  return new_myaccounts

def save_accounts(myaccounts):
  '''
  Function to save contact
  '''
  myaccounts.save_account()

def delete_accounts(myaccounts):
  '''
  Function to delete an account
  '''
  myaccounts.delete_account()

def find_account(name):
  '''
  Function that finds an account by account-name and returns the account
  '''
  return Accounts.find_by_name(name)

def view_existing_accounts(name):
  '''
  Function that check if an account exists with account name and return a boolean
  '''
  return Accounts.account_exists(name)

def display_accounts():
  '''
  Function that returns all saved 
  '''
  return Accounts.display_all_accounts()

def generatePassword(num):
  password = ' '

  for rndm in range(num):
    selected = random.randint(0,94)
    password += string.printable[selected]

  return password

def main():
  print("Hi there, welcome to password-Loc. Please create an account")
  print('\n')

  loc_username = input("Enter Password-Loc username: ")
  loc_password = input("Type in your password: ")
  
  print(f"Hello {loc_username}. Please Re-Type in your password to continue")
  print('\n')

  password_confrim = input("Re-type password: ")

  while password_confrim == loc_password:

    print("Awesome! Select from the short-code options to begin: ca - create new account details, ac - Add new account details, fa - find account details, da - display accounts saved, dl - delete an account record, lo - log out of Password-Loc account")

    option = input().lower()

    if option == 'ac':
      print("Add Account details")
      print("-"*10)

      print("Account name: ")
      account = input()
      print("Account's username: ")
      usr_name = input()
      print("Acount's password")
      a_password = input()

      save_accounts(add_account(account,usr_name,a_password)) # add and save new account.
      print ('\n')
      print(f"New Account {account} added")
      print ('\n')  

    elif option == 'ca':
      print("New Account details")
      print("-"*10)

      print("Account name: ")
      account = input()
      print("Account's username: ")
      usr_name = input()
      print("Acount's password")
      a_password = generatePassword(12)
      print(f"Your a_password will be {a_password}")

      save_accounts(add_account(account,usr_name,a_password)) # add and save new account.
      print ('\n')
      print(f"New Account {account} added")
      print ('\n')  

    elif option == "da":
      if display_accounts():
          print("These are the accounts saved currently.")
          print('\n')

          for account in display_accounts():
            print(f"{account.account_name} {account.username} .....{account.password}")

            print('\n')
      else:
        print('\n')
        print("No accounts added so far!")
        print('\n')

    elif short_code == 'fa':
      print("Enter the account name you wish to search for: ")

      search_name = input()
      if check_existing_contacts(search_name):
        search_account = find_account(search_name)
        print(f"{search_account.account_name} {search_account.username}")
        print('-' * 20)

        print(f"Account's password.......{search_account.password}")
        
      else:
        print("That account not found!")

    elif short_code == 'dl':
      print("Enter the account name you wish to delete: ")

      search_name = input()
      if check_existing_contacts(search_name):
        search_account = find_account(search_name)
        print(f"You prompted to delete {search_account.account_name} account. \n Continue? [y/n]")

        confirm = input()
        if confirm == 'y':
          delete_accounts(search_account)
          print('-' * 20)

          print(f"Account.......{search_account.account_name} has been deleted.")
        else:
          print("Action Aborted!")

    elif short_code == "lo":
      print("Logging out .......")
      break
    else:

      print("Wrong short code option! Refer to the list provided and retype.")   

if __name__ == '__main__':
  main()

