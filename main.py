from datareader.DataReader import DataReader
# import networkx as nx
#
# G = nx.Graph()
#
#
# # G.add_nodes_from(['J','Z','K','Q','S'])
#
# G.add_edge('J', 'Q', weight=5)
# G.add_edge('Z', 'Q', weight=12)
# G.add_edge('Z', 'K', weight=3)
# G.add_edge('S','Z', weight=7)
# G.add_edge('J', 'K', weight=1)
# G.add_edge('Q', 'K', weight=5)
#
# ## retrieve the information
# print(G.adj['K'])

reader = DataReader()

edges = reader.readData("C://Users//moham//Downloads//amazon//com-amazon.ungraph.txt", "Amazon")

print(edges[0].getVertex() + " , " + edges[0].getEdge())