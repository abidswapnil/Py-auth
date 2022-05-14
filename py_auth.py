# simple authentication model by python
with open('test.py', 'r') as f:
    read_file = f.read()
item_1 = read_file.split('\n')[11]

new_file = ''
print(item_1)

# 3 test cases

# Here user_dict has to be overwritten after new registration everytime.
user_dict = {'username': ['abid', 'rafa', 'nira', 'raka', 'disha'], 'key': [123, 345, 345, 123, 123]}

try:
    class User:
        def __init__(self, username, key):
            self.username = username
            self.key = key

        # A class method is a method that is bound to a class
        # rather than its object. It doesn't require creation of a
        # class instance, much like staticmethod.

        @classmethod
        def signUp(cls, new_username, new_key):                                                                 # checking if username in the dictionary or not
            if new_username in user_dict.get('username'):
                print('\nThis name already used.\nUse another name ')
                User.signUp(new_username=str(input('username: ')), new_key=int(input('key: ')))

            else:
                user_dict.get('username').append(new_username)
                user_dict.get('key').append(new_key)
                item_2 = f"user_dict = {user_dict}"
                new_file = read_file.replace(str(item_1), str(item_2))
                with open('test.py', 'w') as f:
                    f.write(new_file)                                                                           # overwriting the file with updated user_dict
                    print(f'hey {new_username}, you are registered now!\nrun the program again for logging in.')

        def logIn(self):
            try:
                index = user_dict.get('username').index(self.username)
                given_key = user_dict.get('key')[index]
                if self.key == given_key:
                    print(f'{self.username} is logged in')

                    def makePost(post):
                        print(f'{post} -by {self.username}')

                    makePost(post=str(input('post: ')))
                else:
                    print('wrong password!!')
            except ValueError:
                print('\nInvalid username!!\nregister here.')
                User.signUp(new_username=str(input('username: ')), new_key=int(input('key: ')))


    user = User(username=str(input('username: ')), key=int(input('key: ')))
    user.logIn()
except ValueError:
    print('username(string), key(integer) \nrun again!')
