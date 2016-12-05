# John Liao
# CS 566, HW 6
# Email: jsmiao@bu.edu
# BU ID: U47-74-9883

"""
Implement (i.e., code and execute), in a language of your choice, Prim's algorithm for finding
the minimum spanning tree of a given graph. Do not use hardcoding, that is, the program should
be able to handle any size. Choose appropriate inputs. Show the result of running your code on
the graph in Figure 23.1 (p. 625) of the textbook. Indicate, with brief justification, whether
the approach is greedy.

Response:
Approach is considered greedy because only the adjacent neighbor weights are considered when
selecting the next edge to be traversed.
"""

import string
import math
import random
import matplotlib.pyplot as plt
import networkx as nx


class Graph:

    def __init__(self):
        self.G = nx.Graph()

        self.total_nodes = 6                     # Number of nodes to be added to Graph
        self.total_edges = 10                    # Number of edges to be added to Graph

        self.nodes = []
        self.edges = []
        self.weight_range = [1, 2, 3, 4, 5]     # Edge weight range setting for Graph generation

        self.prim_edges = []
        self.prim_seed = None

    def generate_graph(self):
        """Generates a random connected graph"""

        self.generate_nodes()
        self.add_edges()
        self.prim()

    def generate_nodes(self):
        """Generate nodes with labels: 'A', 'B', 'AA', 'BB'...'ZZZ'"""

        for i in range(0, self.total_nodes):
            letter = string.ascii_uppercase[i - 26 * int((math.floor(i / 26)))]
            self.nodes.append(letter * int((math.floor(i / 26) + 1)))

    def edge_exists(self, edge_one, edge_two):
        """Returns True if edge already exists in the graph, else return False."""

        for edge in self.edges:
            e1, e2 = edge

            if (e1 == edge_one and e2 == edge_two) or (e2 == edge_one and e1 == edge_two):
                return True

        return False

    def add_edges(self):
        """Adding edges between generated nodes"""

        edges_added = 0

        while edges_added < self.total_edges:
            edge_one = random.choice(self.nodes)
            edge_two = random.choice(self.nodes)

            if edge_one == edge_two:
                continue

            if self.edge_exists(edge_one, edge_two):
                continue

            self.G.add_edges_from([(edge_one, edge_two)], weight=random.choice(self.weight_range))

            self.edges.append((edge_one, edge_two))

            edges_added += 1

        assert nx.number_of_nodes(self.G) == len(self.nodes), 'Not all the nodes were connected. Please try again.'
        assert nx.is_connected(self.G) is True, 'There are insufficient edges to generate a connected graph.'

    def plot(self):
        """Plot the graph that was generated"""

        values = ['white' if node is not self.prim_seed else 'red' for node in self.G.nodes()]          # Seed is set red
        edge_labels = dict([((u, v,), d['weight']) for u, v, d in self.G.edges(data=True)])
        edge_colors = ['black' if not edge in self.prim_edges else 'red' for edge in self.G.edges()]    # Traverse edges are set red

        pos = nx.spring_layout(self.G)
        node_labels = {node: node for node in self.G.nodes()}
        nx.draw_networkx_labels(self.G, pos, labels=node_labels)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        nx.draw(self.G, pos, node_color=values, node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)

        try:
            plt.show()
        except Exception, e:
            print e

    def prim(self):
        """Prim Algorithm to find minimum spanning tree for a weighted undirected graph."""

        seed = random.choice(self.nodes)    # Randomly select 'root'
        visited_nodes = {seed}              # Put seed node in 'visited' bucket
        unvisited_nodes = set(self.nodes)   # Set all other nodes to 'unvisited'
        unvisited_nodes.remove(seed)        # Don't forget to remove the seed node we just added

        self.prim_seed = seed               # Save seed for display purposes

        while len(unvisited_nodes) > 0:
            neighbors = []

            for node_from in visited_nodes:
                for node_to in self.G.neighbors(node_from):
                    if node_to not in visited_nodes:
                        neighbors.append((node_from, node_to, self.G.edge[node_from][node_to]['weight']))

            min_node_to, min_node_from = None, None
            min_weight = 999

            for neighbor in neighbors:
                node_from, node_to, weight = neighbor

                if weight < min_weight:
                    min_node_from = node_from
                    min_node_to = node_to
                    min_weight = weight


            # Save this edge as Traversed
            self.prim_edges.append((min_node_from, min_node_to))      # Save as (A,B) and (B,A)...
            self.prim_edges.append((min_node_to, min_node_from))

            unvisited_nodes.remove(min_node_to)
            visited_nodes.add(min_node_to)

        return

if __name__ == '__main__':
    graph = Graph()
    graph.generate_graph()
    graph.plot()
