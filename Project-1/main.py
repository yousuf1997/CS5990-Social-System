import random

from DataReader import DataReader
from NetworkBuilder import NetworkBuilder
import networkx as nx
import matplotlib.pyplot as plt

random_graph = nx.erdos_renyi_graph(100, 0.4)

edges = random_graph.edges

print(len(edges))
