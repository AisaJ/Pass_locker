#!/usr/bin/env python3.6
from myAccounts import Accounts

def add_account(account,usr_name,a_password):
  '''
  Function to add new account details
  '''
  new_myaccounts = Accounts(account,usr_name,a_password)
  return new_myaccounts

def save_accounts()

