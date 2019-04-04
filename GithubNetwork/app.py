'''
GithubNetwork : Visualize your github social Network!

file: app.py

brief: entry point and dispatcher for the github-network application

https://github.com/AlexanderJDupree/GithubNetwork
'''

__author__    = "Alexander DuPree"
__copyright__ = "Copyright (c) 2019 Alexander DuPree"
__license__   = "MIT"
__version__   = "0.0.1-alpha"
__status__    = "Development"

from os import sys
from .helpers import cmdParser 

def main():

    print(cmdParser.parse(sys.argv[1:]))
    return 0


