'''
file: test_user.py

brief: Unit tests for GithubNetwork API request class

https://github.com/AlexanderJDupree/GithubNetwork

'''

import json
import unittest
from GithubNetwork.helpers.GitHubAPI import User

def loadData(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
    return []

class TestUser(unittest.TestCase):

    data = loadData('test/test_data.json')
    users = [User(user) for user in data]

    def testUserLogin(self):
        user = User(self.data[0])

        self.assertEqual(user.login(), self.data[0]['login'])

    def testUserSet(self):

        # Set 1 and 2 overlap the union should result in the original list
        set1 = self.users[:int(len(self.users)/2)]
        set2 = self.users[int(len(self.users)/3):]
        union = set(set1).union(set2)

        # Wrap the original list as a set to ensure ordering is the same for the test
        self.assertEqual(union, set(self.users))

if __name__ == '__main__':
    unittest.main()

