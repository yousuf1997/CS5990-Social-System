import threading
from NetworkBuilder import NetworkBuilder
from DataReader import  DataReader
from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt

networkBuilder = NetworkBuilder()
dataReader = DataReader()

'''
    srun -n 1 --ntasks-per-node=1 -p gpu -J twitchW --mem-per-cpu=MaxMemPerCPU -u python TwitchWatts.py > twitchWatts.txt
'''

## the following code reads the amazon data
## construct the graph as per the edges in the data
originalNetworkOfTwitchRawData = dataReader.readData("Data/large_twitch_edges.csv", "Twitch")
originalNetworkOfTwitch = networkBuilder.buildGraph(originalNetworkOfTwitchRawData)


def watts():
    wGraph = networkBuilder.generateWattsStrogatzNetwork(originalNetworkOfTwitch, K=10, beta=0.1)
    nx.draw(wGraph)
    plt.show()
    print(wGraph.adj)
watts()
