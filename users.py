class Users:
  '''
  Class that generates new instances of users
  '''

  usersList = []

  def __init__(self,loc_username,loc_password):
    '''
    Defining attributes of the class
    '''
    self.loc_username = loc_username
    self.loc_password = loc_password


  def save_users(self):
    '''
    Adding application users to the list
    '''
    Users.usersList.append(self)