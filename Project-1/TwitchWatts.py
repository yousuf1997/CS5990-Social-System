import threading
from NetworkBuilder import NetworkBuilder
from DataReader import  DataReader
from tabulate import tabulate

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
    wattsModelOfTwitchData = networkBuilder.generateWattsStrogatzNetwork(originalNetworkOfTwitch, K=1000, beta=0.001)
    print("Twitch Data Analytics Of Watts Graph : Average Path Length " + str(networkBuilder.computeAveragePathLength(wattsModelOfTwitchData)))
    print("Twitch Data Analytics Of Watts Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(wattsModelOfTwitchData)))


watts()
