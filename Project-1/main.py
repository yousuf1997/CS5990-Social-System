import random

from DataReader import DataReader
from NetworkBuilder import NetworkBuilder
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


# G.add_nodes_from(['J','Z','K','Q','S'])

G.add_edge('J', 'Q')
G.add_edge('Z', 'Q')
G.add_edge('Z', 'K')
G.add_edge('S','Z')
G.add_edge('J', 'K')
G.add_edge('Q', 'K')
#
# ## retrieve the information
# print(G.adj)
# print(G.size())
networkBuilder = NetworkBuilder()
networkBuilder.calculateAverageClusteringCoefficient(graph=G)
# nodes = []
# index = 0
# while index < 10:
#     nodes.append(random.randint(0, 100))
#     index = index + 1
#
# reader = DataReader()
# edges = reader.readData("C://Users//moham//Downloads//amazon//com-amazon.ungraph.txt", "Amazon")
# amazonGraph = networkBuilder.buildGraph(edges)
#
# ring = networkBuilder.generateBarabasiAlbertNetwork(list(amazonGraph.nodes), 1000)
# #
# nx.draw(ring, with_labels=True, pos=nx.spiral_layout(ring))
# plt.show()
# latticeGraph = networkBuilder.generatRegularRingLatticeGraph(G, 4)
# print(G.adj['J'])
# print(sorted(G.nodes))
reader = DataReader()
edges = reader.readData("C://Users//moham//Downloads//amazon//com-amazon.ungraph.txt", "Amazon")
amazonGraph = networkBuilder.buildGraph(edges)
wattsGraph = networkBuilder.generateWattsStrogatzNetwork(graph=G, K=10, beta=0.001)

# # #
# # #
# #
# # amazonGraph = networkBuilder.buildGraph(edges)
# #
# # print("Average degree of amazon network data set >> " + str(networkBuilder.computeAverageDegree(amazonGraph)))
# # print("Network size is >> " + str(networkBuilder.computeNetworkSize(amazonGraph)))

