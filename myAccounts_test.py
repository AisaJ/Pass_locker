import unittest #importing the unittest module
from myAccounts import Accounts #importing accounts class
import pyperclip


class TestAccounts(unittest.TestCase):

  '''
  Test class that defines test cases for the accounts class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def tearDown(self):
    '''
    This method does clean up after each test case has run.
    '''
    Accounts.accounts_list = []

  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_myaccounts = Accounts("LinkedIn","Jammy","jem#jem") #create account object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_myaccounts.account_name,"LinkedIn")
    self.assertEqual(self.new_myaccounts.username, "Jammy")
    self.assertEqual(self.new_myaccounts.password, "jem#jem")

  def test_save_account(self):
    '''
    Test case to test if the accounts object is saved in the myaccounts list
    '''
    self.new_myaccounts.save_account()
    self.assertEqual(len(Accounts.accounts_list),1)

  def test_multiple_accounts(self):
    '''
    Test case to check if we can save multiple contacts
    '''
    self.new_myaccounts.save_account()
    test_myaccounts = Accounts("Twitter","Jammy","jam#jam")
    test_myaccounts.save_account()
    self.assertEqual(len(Accounts.accounts_list),2)

  def test_delete_accounts(self):
    '''
    Test case for removing unwanted accounts from accounts-list
    '''
    self.new_myaccounts.save_account()
    test_myaccounts = Accounts("Twitter","Jammy","jam#jam")
    test_myaccounts.save_account()
    self.new_myaccounts.delete_account()
    self.assertEqual(len(Accounts.accounts_list),1)

  def test_display_all_accounts(self):
      '''
      method that returns a list of all accounts saved
      '''
      self.assertEqual(Accounts.display_all_accounts(),Accounts.accounts_list)

  def test_find_account_by_name(self):
    '''
    Test case to check if we can find account details by account name and display the information
    '''
    self.new_myaccounts.save_account()
    test_myaccounts = Accounts("Twitter","Jammy","jam#jam")
    test_myaccounts.save_account()
    found_account = Accounts.find_by_name("Twitter")
    self.assertEqual(found_account.password,test_myaccounts.password)

  def test_account_exists(self):
    '''
    test to check if we can return a Boolean  if we cannot find the contact.
    '''
    self.new_myaccounts.save_account()
    test_myaccounts = Accounts("Twitter","Jammy","jam#jam")
    test_myaccounts.save_account()
    account_exists = Accounts.account_exists("Twitter")

    self.assertTrue(account_exists)

  def test_copy_credentilas(self):
    '''Test case to confirm we are copying username and password from account found
    '''
    self.new_myaccounts.save_account()
    Accounts.copy_username("jammy")
    Accounts.copy_password("jam#jam")
    self.assertEqual(self.new_myaccounts.username,self.new_myaccounts.password,pyperclip.paste())
    

if __name__ == '__main__':
  unittest.main()
