'''
file: test_parser.py

brief: Unit tests for GithubNetwork command line parser

https://github.com/AlexanderJDupree/GitHubNetwork
'''

import argparse
import unittest
from GithubNetwork.helpers import cmdParser as parser

class TestCommandParser(unittest.TestCase):

    ''' Command line options '''
    options = ['user','diameter', 'max', 'vis', 'output', 'labels', 
               'arrowsize', 'scale', 'normalize', 'colored', 'width',
               'figsize', 'axis']

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
        defaultVals = [
                'USER', 5, 500, 'spring', 'network.png', False, 10, 1.0, False, True, 1.0,
                (20, 20), False
                ]
        expectedDict = dict(zip(self.options, defaultVals))

        self.assertEqual(expectedDict, parser.parse(['USER']))

if __name__ == '__main__':
    unittest.main()

