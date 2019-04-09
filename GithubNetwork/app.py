'''
GithubNetwork : Visualize your github social Network!

file: app.py

brief: entry point and dispatcher for the github-network application

https://github.com/AlexanderJDupree/GithubNetwork
'''

__author__    = "Alexander DuPree"
__copyright__ = "Copyright (c) 2019 Alexander DuPree"
__license__   = "MIT"
__version__   = "1.0.0a"
__status__    = "Development"

from os import sys
from .helpers import cmdParser, GitHubAPI as API
from .helpers.graph import GitHubNetwork

def main():

    args = cmdParser.parse(sys.argv[1:])

    graph = GitHubNetwork(args['diameter'], args['max'])

    graph.mapNetwork(args['user'])

    graph.draw(
            output_file = args['output'],
            arrowsize   = args['arrowsize'],
            scale       = args['scale'],
            width       = args['width'],
            normalize   = args['normalize'],
            colored     = args['colored'],
            labels      = args['labels'],
            layout      = args['vis'],
            axis        = args['axis'],
            figsize     = args['figsize']
            )

    # Remove file extension if provided
    graph.write(args['output'].split('.')[0], args['format'])

    return 0

