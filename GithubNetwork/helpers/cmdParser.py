'''
file: cmdParser.py

brief: cmdParser validates command line args and parses them into a dict object

https://github.com/AlexanderJDupree/GithubNetwork
'''

import argparse

VIS_LAYOUTS = ['circular', 'kamada-kawai', 'random', 
               'spectral', 'spring', 'shell']

def validateInteger(arg, lbound, ubound):
    value = int(arg)
    if value < lbound or value > ubound:
        raise argparse.ArgumentTypeError(
                f'{arg} is not within range {lbound}..{ubound}'
                )
    return value

# TODO bounds have been set arbitrarily. Test actual reasonable bounds for app
def validateDiameter(arg):
    return validateInteger(arg, 1, 10)

def validateMaxNodes(arg):
    return validateInteger(arg, 1, 10000)

def validateArrowSize(arg):
    return validateInteger(arg, 1, 20)

def validateVisualization(arg):
    if arg in VIS_LAYOUTS:
        return arg
    else:
        raise argparse.ArgumentTypeError(
                '{} is not an accepted layout. Accepted layouts are: \n\t{}'.format(
                    arg, '\n\t'.join(VIS_LAYOUTS))
                )

def parse(argv):

    parser = argparse.ArgumentParser(
            description="Visualize your your GitHub social network!"
            )
    parser.add_argument( # TODO make username optional
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
            default='spring',
            help="Graph visualization <LAYOUT>. Default=spring. Layouts are \n\t{}".format(
                '\n\t'.join(VIS_LAYOUTS))
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
            metavar='', 
            default=False,
            help="Normalize the size of each node. Default=False"
            )
    parser.add_argument(
            '-c', '--colored',
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
            '-r', '--read',
            metavar='',
            default=None,
            help="Read a <GRAPHML FILE> instead of polling GitHubAPI. Default=None"
            )

    #TODO Add figsize tuple argument

    # Returns a dict object
    return vars(parser.parse_args(argv))

