'''
file: user.py

brief: User class represents a GitHub user account. Holds data such as login 
       name, id, and a list of followers/following
'''

class User:

    def __init__(self, data, followers, following):
        self._data = data
        self._following = following
        self._followers = followers

    def login(self):
        return self._data['login']

    def avatar_url(self):
        return self._data['avatar_url']

    def id(self):
        return self._data['id']

    def followers(self):
        return [data['login'] for data in self._followers]

    def __repr__(self):
        return "login: " + self.login() + " id: " + str(self.id())

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.id() == other.id()

    def __hash__(self):
        return self.id()

