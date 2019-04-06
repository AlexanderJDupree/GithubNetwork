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

def main():

    args = cmdParser.parse(sys.argv[1:])

    user = API.getUser(args['user'])

    graph = nx.DiGraph()

    for follower in user.followers():
        graph.add_edge(follower, user.login())

    for username in user.following():
        graph.add_edge(user.login(), username)

    pos = nx.spectral_layout(graph)

    betCent = nx.betweenness_centrality(graph, normalized=True, endpoints=True)

    node_color = [20000.0 * graph.degree(v) for v in graph]
    node_size =  [v * 15000 for v in betCent.values()]

    plt.figure(figsize=(15, 15))
    nx.draw_networkx(graph, pos, node_color=node_color, node_size=node_size, cmap=plt.cm.coolwarm, arrowsize=20, font_weight='bold')

    plt.axis('off')
    plt.savefig("test.png", format="PNG")

    return 0

