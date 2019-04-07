'''
file: graph.py

brief: Constructs the graph from the GithubAPI and utilizes networkx and 
       matplotlib to draw and save the graph to a png file

https://github.com/AlexanderJDupree/GithubNetwork
'''

import multiprocessing
import networkx as nx
import matplotlib.pyplot as plt
from requests.exceptions import HTTPError
from .GitHubAPI import *

class Graph:

    _layouts = {
            'shell'        : nx.shell_layout,
            'random'       : nx.random_layout,
            'spring'       : nx.spring_layout,
            'circular'     : nx.circular_layout,
            'spectral'     : nx.spectral_layout,
            'kamada-kawai' : nx.kamada_kawai_layout
            }
    
    def __init__(self, diameter, maxNodes):
        self._diameter  = diameter
        self._maxNodes  = maxNodes
        self._graph     = nx.DiGraph()

    def draw(self, output_file, arrowsize=10, scale=1.0, width=1.0, 
             normalize=False, colored=True, labels=True, layout='spring'):

        pos = self._layouts[layout](self._graph)

        node_color = self._nodeColor(colored)
        node_size = self._nodeSize(normalize, scale)

        # TODO parameterize figsize
        plt.figure(figsize=(20, 20))
        nx.draw_networkx(self._graph, pos, node_color=node_color, node_size=node_size, 
                         with_labels=labels, arrowsize=arrowsize, width=width)

        plt.axis('off')
        plt.savefig(output_file, format="PNG")
        return

    def _nodeColor(self, colored):
        return [20000.0 * self._graph.degree(v) for v in self._graph] if colored else 'r'

    def _nodeSize(self, normalize, scale):
        return int(300 * scale) if normalize else [v * 10100 for v in self._betCent().values()]

    def _betCent(self):
        return nx.betweenness_centrality(self._graph, endpoints=True)

    # TODO parameterize file types
    def write(self, output_file):
        nx.write_graphml_xml(self._graph, output_file + ".graphml")

    def read(self, input_file):
        self._graph = nx.read_graphml(input_file)
        return

    def mapNetwork(self, username):

        self._mapNetwork(username, self._diameter)
        return

    def _mapNetwork(self, username, depth):
        if depth <= 0 or self._graph.number_of_nodes() >= self._maxNodes:
            return 

        try:
            user = getUser(username)
            self.__mapNetwork(user, depth - 1)
        except HTTPError:
            #TODO Set option to log failed usernames
            return

    # TODO clean up and optimize
    def __mapNetwork(self, user, depth):

        followers = user.followers()
        following = user.following()
        union = set(followers).union(following)

        edge_list = zip(followers, [user.login() for i in range(len(followers))])

        self._graph.add_edges_from(edge_list)

        edge_list = zip([user.login() for i in range(len(following))], following)

        self._graph.add_edges_from(edge_list)

        # Only instantiate processes for first level of recursion
        if(depth == self._diameter):
            # TODO review number of processes to use
            # Taks and chunksize are limited to 1 to free memory after each recursive branch
            with multiprocessing.Pool(processes=4, maxtasksperchild=1) as pool:
                # starmap unpacks the union and depth as key, value pairs
                pool.starmap(self._mapNetwork, 
                             zip(union, [depth for i in range(len(union))]),
                             chunksize=1)
                pool.close()
                pool.join()
        else:
            for user in union:
                self._mapNetwork(user, depth)
        return

