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
from .helpers import cmdParser, GitHubAPI as API
from .helpers.graph import Graph

def main():

    args = cmdParser.parse(sys.argv[1:])

    graph = Graph(args['diameter'], args['max'])

    # TODO provide updates and progress bars
    if args['read']:
        graph.read(args['read'])
    else:
        graph.mapNetwork(args['user'])

    graph.draw(args['output'], args['arrowsize'], args['scale'], args['width'],
               args['normalize'], args['colored'], args['labels'], args['vis'])

    graph.write(args['output'].split('.')[0])

    return 0
