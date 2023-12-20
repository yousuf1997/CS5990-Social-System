import threading

from networkx import Graph

from NetworkBuilder import NetworkBuilder
import networkx as nx
import matplotlib.pyplot as plt
import time
import concurrent.futures
import numpy
from multiprocessing import Pool
# Number of nodes and edges
num_nodes = 100
num_edges = 400  # You can adjust this number as needed

# Create a random graph with 50 nodes and 100 edges
G = nx.gnm_random_graph(num_nodes, num_edges, directed=False)

networkBuilder = NetworkBuilder()

wGraph = networkBuilder.generateBarabasiAlbertNetwork(vertices=list(G.nodes), K=10)

# nx.draw(wGraph)
# plt.show()

print(wGraph.adj)