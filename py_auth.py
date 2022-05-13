# simple authentication model by python

x = 0
# 3 test cases
while x <= 2:
    # Here user_dict has to be overwritten after new registration everytime.
    user_dict = {
        'username': ['abid', 'tasnim', 'sara'],
        'key': [123, 345, 678]
    }

    try:
        class User:
            def __init__(self, username, key):  #
                self.username = username
                self.key = key

            # A class method is a method that is bound to a class
            # rather than its object. It doesn't require creation of a
            # class instance, much like staticmethod.

            @classmethod
            def signUp(cls, new_username, new_key):  # checking if username in the dictionary or not
                if new_username in user_dict.get('username'):
                    print('\nThis name already used.\nUse another name ')
                    User.signUp(new_username=str(input('username: ')), new_key=int(input('key: ')))

                else:
                    user_dict.get('username').append(new_username)
                    user_dict.get('key').append(new_key)

            def logIn(self):
                try:
                    index = user_dict.get('username').index(self.username)
                    given_key = user_dict.get('key')[index]
                    if self.key == given_key:
                        print(f'{self.username} is logged in')

                        def makePost(post):
                            print(f'{post} by {self.username}')

                        makePost(post=str(input('post: ')))
                    else:
                        return False
                except ValueError:
                    print('\nInvalid username password!!\nregister here.')
                    User.signUp(new_username=str(input('username: ')), new_key=int(input('key: ')))


        user = User(username=str(input('username: ')), key=int(input('key: ')))
        user.logIn()
        print(user_dict)
    except ValueError:
        print('username(string), key(integer) \nrun again!')
        x += 1
