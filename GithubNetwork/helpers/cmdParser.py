'''
file: cmdParser.py

brief: cmdParser validates command line args and parses them into a dict object

https://github.com/AlexanderJDupree/GithubNetwork
'''

import argparse

VIS_LAYOUTS = ['circular', 'kamada-kawai', 'random', 'spectral', 'spring', 'shell']

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
    return validateInteger(arg, 1, 1000)

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
            help="<NUMBER> length of the longest shortest path from the user"
            )
    parser.add_argument(
            '-m', '--max',
            type=validateMaxNodes,
            metavar='',
            default=200,
            help="max <NUMBER> of nodes in the graph"
            )
    parser.add_argument(
            '-v', '--vis',
            choices=VIS_LAYOUTS,
            metavar='',
            default='kamada-kawai',
            help="Graph visualization <LAYOUT>. Layouts are \n\t{}".format(
                '\n\t'.join(VIS_LAYOUTS))
            )
    parser.add_argument(
            '-o', '--output',
            metavar='',
            default='network.png',
            help='Desired <FILE NAME> of output'
            )

    # Returns a dict object
    return vars(parser.parse_args(argv))

