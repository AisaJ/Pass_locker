class Accounts:
  '''
  Class that generates new instances of accounts
  '''
  accounts_list = []
  def save_account(self):
    '''
    save_account method saves account objects into accounts_list
    '''
    Accounts.accounts_list.append(self)

  def __init__(self, account_name,username,password):
    self.account_name = account_name
    self.username = username
    self.password = password
    



