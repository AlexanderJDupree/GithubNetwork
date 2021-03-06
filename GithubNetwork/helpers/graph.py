'''
file: graph.py

brief: Constructs the graph from the GithubAPI and utilizes networkx and
       matplotlib to draw and save the graph to a png file

https://github.com/AlexanderJDupree/GithubNetwork
'''

import networkx as nx

import matplotlib as mpl
mpl.use('Agg') # Tk backend does not seem to be as prevalent as Agg backend

import matplotlib.pyplot as plt
from tqdm import tqdm
from requests.exceptions import HTTPError
from .GitHubAPI import *

class GitHubNetwork:

    _layouts = {
            'shell'        : nx.shell_layout,
            'random'       : nx.random_layout,
            'spring'       : nx.spring_layout,
            'circular'     : nx.circular_layout,
            'spectral'     : nx.spectral_layout,
            'kamada-kawai' : nx.kamada_kawai_layout
            }
    _formats = {
            'graphml'        : (nx.write_graphml_xml, '.graphml'),
            'adjacency_list' : (nx.write_adjlist, '.adjlist'),
            'edge_list'      : (nx.write_edgelist, '.edgelist'),
            'pickle'         : (nx.write_gpickle, '.gpickle'),
            'yaml'           : (nx.write_yaml, '.yaml'),
            'gexf'           : (nx.write_gexf, '.gexf')
            }
    _colormaps = {
            'rainbow'    : plt.cm.rainbow,
            'purples'    : plt.cm.Purples,
            'greys'      : plt.cm.Greys,
            'blues'      : plt.cm.Blues,
            'greens'     : plt.cm.Greens,
            'yellow-red' : plt.cm.YlOrRd,
            'spring'     : plt.cm.spring,
            'summer'     : plt.cm.summer,
            'cool'       : plt.cm.cool, 
            'hot'        : plt.cm.hot, 
            'gnuplot'    : plt.cm.gnuplot,
            'twilight'   : plt.cm.twilight,
            'coolwarm'   : plt.cm.coolwarm
            }
    
    def __init__(self, diameter, maxNodes):
        self._diameter  = diameter
        self._maxNodes  = maxNodes
        self._graph     = nx.DiGraph()
        self._processed = set()

    def draw(self, output_file, arrowsize=10, scale=1.0, width=1.0, figsize=(20, 20),
             normalize=False, labels=True, axis=False, colorbar=True, layout='spring', 
             cmap='rainbow'):

        pos = self._layouts[layout](self._graph)

        node_color = self._nodeColor()
        node_size = self._nodeSize(normalize, scale)

        cmap = self._colormaps[cmap]
        vmin = min(node_color)
        vmax = max(node_color)

        plt.figure(figsize=figsize)

        # TODO this can take awhile, add progress update or a 'hang in there'
        nx.draw_networkx(self._graph, pos, node_color=node_color, node_size=node_size,
                         cmap=cmap, vmin=vmin, vmax=vmax, with_labels=labels, 
                         arrowsize=arrowsize, width=width)

        if(colorbar == True):
            sm = plt.cm.ScalarMappable(cmap=cmap,
                                       norm=plt.Normalize(vmin=vmin, vmax=vmax))
            sm._A = []
            plt.colorbar(sm)

        if(axis == False):
            plt.axis('off')

        plt.savefig(output_file, format="PNG")
        return

    def _nodeColor(self):
        # TODO add different ways to represent color mapping
        return [self._graph.degree(v) for v in self._graph]

    def _nodeSize(self, normalize, scale):
        # TODO add different ways to represent node size mappings
        return int(300 * scale) if normalize else [v * 10100 for v in self._betCent().values()]

    def _betCent(self):
        return nx.betweenness_centrality(self._graph, endpoints=True)

    # TODO parameterize file type and add different output types
    def write(self, output_file, file_format):
        # Function and extension lookup
        nx_write  = self._formats[file_format][0]
        extension = self._formats[file_format][1]

        nx_write(self._graph, output_file + extension)

    def mapNetwork(self, username):

        try:
            user = getUser(username)
        except HTTPError:
            return #TODO helpful error message

        self._mapNetwork(user, self._diameter)
        # Empty hash set of processed data
        self._processed.clear()
        return

    def _mapNetwork(self, user, depth):

        if depth <= 0 or self._graph.number_of_nodes() >= self._maxNodes or user in self._processed:
            return

        self._addFollowers(user)
        self._addFollowing(user)

        union = set(user.followers()).union(user.following())

        self._processed.add(user)

        for user in tqdm(union, desc="Mapping {}".format(user.login())):
            self._mapNetwork(user, depth - 1)
        return

    def _addFollowers(self, user):
        for follower in tqdm(user.followers(), desc="Writing {} followers to graph".format(user.login())):
            self._graph.add_edge(follower, user)
        return

    def _addFollowing(self, user):
        for following in tqdm(user.following(), desc="Writing {} following to graph".format(user.login())):
            self._graph.add_edge(user, following)
        return

