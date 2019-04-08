class Users:
  '''
  Class that generates new instances of users
  '''
  def __int__(self,loc_username,loc_password):
    '''
    Defining attributes of the class
    '''
    self.loc_username = loc_username
    self.loc_password = loc_password

    usersList = []

  def save_users(self):
    '''
    Adding application users to the list
    '''
    Users.usersList.append(self)