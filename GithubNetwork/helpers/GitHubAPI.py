'''
file: GitHubAPI.py

brief: Defines a wrapper class for the GitHub RESTful API. Handles all HTTPS
       requests and exception handling of those requests.

https://github.com/AlexanderJDupree/GithubNetwork
'''

import os
import requests

GITHUB_API = "https://api.github.com/"
USER = os.environ['GITHUB_USER'] if 'GITHUB_USER' in os.environ.keys() else ''
PASS = os.environ['GITHUB_PASS'] if 'GITHUB_PASS' in os.environ.keys() else ''

def _API_Request(request):
    response = requests.get(request, auth=(USER, PASS))

    return _validateResponse(response)

def _validateResponse(response):

    # TODO detailed error message
    response.raise_for_status()

    return response.json()

def getUser(username):

    response = _API_Request(GITHUB_API + "users/" + username)

    return User(response)

def getFollowers(followers_url):

    try:
        followers = _API_Request(followers_url)
    except requests.exceptions.HTTPError:
        followers = []

    return [User(follower) for follower in followers]

class User:

    '''
    User class represents a GitHub user account. Holding data such as login,
    id, and a list of followers/following
    '''

    def __init__(self, data):
        self._data = data
        self._followers = None
        self._following = None

    def login(self):
        return self._data['login']

    def avatar_url(self):
        return self._data['avatar_url']

    def id(self):
        return self._data['id']

    def followers(self):
        if(self._followers == None):
            self._followers = getFollowers(self._data['followers_url'])
        return self._followers

    def following(self):
        if(self._following == None):
            # Raw response has {/other user} optional at end or url
            self._following = getFollowers(self._data['following_url'].split('{')[0])
        return self._following

    def __repr__(self):
        return "login: " + self.login() + " id: " + str(self.id())

    def __str__(self):
        return self.login()

    def __eq__(self, other):
        return self.id() == other.id()

    def __hash__(self):
        return self.id()

