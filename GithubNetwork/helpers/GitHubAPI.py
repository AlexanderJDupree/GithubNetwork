'''
file: GitHubAPI.py

brief: Defines a wrapper class for the GitHub RESTful API. Handles all HTTPS 
       requests and exception handling of those requests.
'''

import requests
from .user import User

GITHUB_API = "https://api.github.com/"

def _API_Request(request):
    response = requests.get(request)

    return _validateResponse(response)

def _validateResponse(response):

    # TODO detailed error message
    response.raise_for_status()

    return response.json()

def getUser(username):

    response = _API_Request(GITHUB_API + "users/" + username)

    followers = _API_Request(response['followers_url'])

    # Raw response has {/other user} optional at end or url
    following = _API_Request(response['following_url'].split('{')[0])

    return User(response, followers, following)

