import random

from DataReader import DataReader
from NetworkBuilder import NetworkBuilder
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("v1", "v2")
G.add_edge("v1", "v4")
G.add_edge("v4", "v3")
G.add_edge("v3", "v2")
G.add_edge("v1", "v3")

print(list(nx.all_triads(G)))

