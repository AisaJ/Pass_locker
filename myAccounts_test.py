import unittest #importing the unittest module
from accounts import Accounts #importing accounts class

class TestAccounts(unittest.TestCase):

  '''
  Test class that defines test cases for the accounts class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_accounts = Accounts("LinkedIn","Aisa","jem#jem") #create account object

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_accounts.account_name,"LinkedIn")
    self.assertEqual(self.new_accounts.username, "Aisa")
    self.assertEqual(self.new_accounts.password, "jem#jem")

if __name__ == '__main__':
  unittest.main()
