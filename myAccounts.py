class Accounts:
  '''
  Class that generates new instances of accounts
  '''
  accounts_list = []
  
  def __init__(self, account_name,username,password):
    self.account_name = account_name
    self.username = username
    self.password = password

  def save_account(self):
    '''
    save_account method saves account objects into accounts_list
    '''
    Accounts.accounts_list.append(self)

  def delete_account(self):
    '''
    This method deletes details of an account from accounts-list
    '''
    Accounts.accounts_list.remove(self)

  @classmethod
  def display_accounts(cls):
    '''
    method that returns the account list
    '''
    return cls.accounts_list

    



