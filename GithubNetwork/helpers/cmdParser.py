'''
file: cmdParser.py

brief: cmdParser validates command line args and parses them into a dict object

https://github.com/AlexanderJDupree/GithubNetwork
'''

import argparse

VIS_LAYOUTS = ['spring', 'kamada-kawai', 'random', 'spectral', 'circular', 'shell']

FILE_FORMATS = [ 'graphml', 'pickle', 'adjacency_list', 'gexf', 'yaml', 'edge_list' ]

def validateInteger(arg, lbound, ubound):
    value = int(arg)
    if value < lbound or value > ubound:
        raise argparse.ArgumentTypeError(
                f'{arg} is not within range {lbound}..{ubound}'
                )
    return value

def validateDiameter(arg):
    return validateInteger(arg, 1, 100)

def validateMaxNodes(arg):
    return validateInteger(arg, 1, 5000)

def validateArrowSize(arg):
    return validateInteger(arg, 1, 20)

def parse(argv):

    parser = argparse.ArgumentParser(
            description="Visualize your your GitHub social network!"
            )
    parser.add_argument(
            'user',
            metavar='USERNAME',
            help="<USERNAME> of a Github profile"
            )
    parser.add_argument(
            '-d', '--diameter',
            type=validateDiameter,
            metavar='',
            default=5,
            help="<NUMBER> length of the longest shortest path from the user. Default=5"
            )
    parser.add_argument(
            '-m', '--max',
            type=validateMaxNodes,
            metavar='',
            default=500,
            help="max <NUMBER> of nodes in the graph. Default=500"
            )
    parser.add_argument(
            '-v', '--vis',
            choices=VIS_LAYOUTS,
            metavar='',
            default=VIS_LAYOUTS[0],
            help="Graph visualization <LAYOUT>. Default={}. Layouts are \n\t{}".format(
                VIS_LAYOUTS[0], '\n\t'.join(VIS_LAYOUTS))
            )
    parser.add_argument(
            '-o', '--output',
            metavar='',
            default='network.png',
            help='Desired <FILE NAME> of output. Default=network.png'
            )
    parser.add_argument(
            '-l', '--labels',
            metavar='',
            default=False,
            help="Display labels with each node. Default=False"
            )
    parser.add_argument(
            '-a', '--arrowsize',
            type=validateArrowSize,
            metavar='',
            default=10,
            help="Specify size of arrows. <NUMBER>. Default=10"
            )
    parser.add_argument(
            '-s', '--scale',
            type=float,
            metavar='',
            default=1.0,
            help="Scale the size of each nodes. <FLOAT>. Default=1.0"
            )
    parser.add_argument(
            '-n', '--normalize',
            type=bool,
            metavar='',
            default=False,
            help="Normalize the size of each node. Default=False"
            )
    parser.add_argument(
            '-c', '--colored',
            type=bool,
            metavar='',
            default=True,
            help="Scale colors by betweeness centrality factor. Default=True"
            )
    parser.add_argument(
            '-w', '--width', 
            type=float,
            metavar='',
            default=1.0,
            help="Width of edge lines <FLOAT>. Default=1.0"
            )
    parser.add_argument(
            '-f', '--figsize',
            type=int,
            nargs=2,
            metavar='',
            choices=range(1, 100),
            default=(20,20),
            help="Figure size tuple: (<WIDTH>,<HEIGHT>), default=(20,20)"
            )
    parser.add_argument(
            '-x', '--axis',
            type=bool,
            metavar='',
            default=False,
            help="Display graphs x/y axis. Default=False"
            )
    parser.add_argument(
            '--format',
            choices=FILE_FORMATS,
            default=FILE_FORMATS[0],
            help="Graph output file format. Default={}.".format(
                FILE_FORMATS[0]
            ))

    # Returns a dict object
    return vars(parser.parse_args(argv))
