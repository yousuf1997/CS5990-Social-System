# from DataReader import DataReader
from NetworkBuilder import NetworkBuilder
import networkx as nx

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

# reader = DataReader()
# #
# edges = reader.readData("C://Users//moham//Downloads//amazon//com-amazon.ungraph.txt", "Amazon")
# #
#
# amazonGraph = networkBuilder.buildGraph(edges)
#
# print("Average degree of amazon network data set >> " + str(networkBuilder.computeAverageDegree(amazonGraph)))
# print("Network size is >> " + str(networkBuilder.computeNetworkSize(amazonGraph)))