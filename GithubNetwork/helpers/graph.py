'''
file: graph.py

brief: Constructs the graph from the GithubAPI and utilizes networkx and 
       matplotlib to draw and save the graph to a png file

https://github.com/AlexanderJDupree/GithubNetwork
'''

import networkx as nx
import GitHubAPI as API
import matplotlib.pylot as plt

class Graph:

    layouts = {
            'shell'        : nx.shell_layout,
            'random'       : nx.random_layout,
            'spring'       : nx.spring_layout,
            'circular'     : nx.circular_layout,
            'spectral'     : nx.spectral_layout,
            'bipartite'    : nx.bipartite_layout,
            'kamada-kawai' : nx.kamada_kawai_layout
            }

    def __init__(diameter, maxNodes, layout, figsize=(20,20)):
        self._diameter = diameter
        self._maxNodes = maxNodes
        self._layout   = layout
        self._figsize  = figsize
        self._graph    = nx.DiGraph()

    def drawNetwork(self, username):
        user_main = API.getUser(username)

        self._crawlNetwork(user_main, self._diameter)

    def _crawlNetwork(self, user, depth):
        if depth <= 0:
            return

        for follower in user.followers():
            self._graph.add_edge(follower, user.login())
            self._crawlNetwork(API.getUser(follower), depth - 1)

        for following in user.following():
            self._graph.add_edge(user.login(), following)
            self._crawlNetwork(API.getUser(following), depth - 1)







