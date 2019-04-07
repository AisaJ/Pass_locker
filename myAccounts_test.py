import unittest #importing the unittest module
from myAccounts import Accounts #importing accounts class


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
    self.new_myaccounts = Accounts("LinkedIn","Aisa","jem#jem") #create account object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_myaccounts.account_name,"LinkedIn")
    self.assertEqual(self.new_myaccounts.username, "Aisa")
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
      method that returns a list of all contacts saved
      '''
      self.assertEqual(Accounts.test_display_all_accounts(),Accounts.accounts_list)


if __name__ == '__main__':
  unittest.main()
