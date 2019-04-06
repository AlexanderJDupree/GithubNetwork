'''
file: test_GitHubAPI.py

brief: Unit tests for GithubNetwork API request class

https://github.com/AlexanderJDupree/GithubNetwork
'''

import unittest
import requests
from GithubNetwork.helpers import GitHubAPI as API

class TestGitHubAPI(unittest.TestCase):

    login = 'AlexanderJDupree'

    def testNothing(self):
        self.assertEqual(1, 1)

    def testGetUserReturnsUserObject(self):

        user = API.getUser(self.login)

        self.assertEqual(self.login, user.login())

    def testGetUserRaises404OnInvalidUsername(self):

        self.assertRaises(requests.exceptions.HTTPError, API.getUser, 'not a user')

if __name__ == '__main__':
    unittest.main()
