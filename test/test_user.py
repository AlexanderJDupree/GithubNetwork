'''
file: test_user.py

brief: Unit tests for GithubNetwork API request class

https://github.com/AlexanderJDupree/GithubNetwork

'''

import json
import unittest
from GithubNetwork.helpers.user import User

def loadData(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
    return []

class TestUser(unittest.TestCase):

    data = loadData('test/test_data.json')
    usernames = [user['login'] for user in data]

    def testUserLogin(self):
        user = User(self.data[0], self.data, self.data)

        self.assertEqual(user.login(), self.data[0]['login'])

    def testFollowers(self):
        user = User(self.data[0], self.data, self.data)

        self.assertEqual(user.followers(), self.usernames)


if __name__ == '__main__':
    unittest.main()

