'''
file: test_parser.py

brief: Unit tests for GithubNetwork command line parser

https://github.com/AlexanderJDupree/github-network
'''

import argparse
import unittest
from GithubNetwork.helpers import cmdParser as parser

class TestCommandParser(unittest.TestCase):

    ''' Command line options '''
    options = ['user','diameter', 'max', 'vis', 'output']
    longopts = [ '{}{}'.format('--', option) for option in options ]
    shortopts = [ '{}{}'.format('-', option[0]) for option in options ]

    def testValidateIntegerUpperBound(self):
        '''Validate integer raises exception on values greater than ubound'''
        self.assertRaises(argparse.ArgumentTypeError, parser.validateInteger, "10", 0, 9)

    def testValidateIntegerLowerBound(self):
        '''Validate integer raises exception on values greater than ubound'''
        self.assertRaises(argparse.ArgumentTypeError, parser.validateInteger, "1", 2, 9)

    def testInvalidIntegerConversion(self):
        ''' Validate integer raises value error when arg fails to convert '''
        self.assertRaises(ValueError, parser.validateInteger, "not a num", 0, 9)

    def testDefaultOptions(self):
        ''' Test the parser returns the default options when none are provided'''
        expectedDict = dict(zip(self.options, ['USER', 5,  200, 'kamada-kawai', 'network.png' ]))

        self.assertEqual(expectedDict, parser.parse(['USER']))

if __name__ == '__main__':
    unittest.main()
