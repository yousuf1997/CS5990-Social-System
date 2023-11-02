import threading
from NetworkBuilder import NetworkBuilder
from DataReader import  DataReader
from tabulate import tabulate

networkBuilder = NetworkBuilder()
dataReader = DataReader()

'''
    srun -n 1 --ntasks-per-node=1 -p gpu -J twitchB --priority="TOP" -u python TwitchBarbasi.py > twitchBarbasi.txt
'''

## the following code reads the amazon data
## construct the graph as per the edges in the data
originalNetworkOfTwitchRawData = dataReader.readData("Data/large_twitch_edges.csv", "Twitch")
originalNetworkOfTwitch = networkBuilder.buildGraph(originalNetworkOfTwitchRawData)


def original():
    print("Twitch Data Analytics Of Original Graph : Average Degree " + str(networkBuilder.computeAverageDegree(originalNetworkOfTwitch)))
    print("Twitch Data Analytics Of Original Graph : Average Path Length " + str(networkBuilder.computeAveragePathLength(originalNetworkOfTwitch)))
    print("Twitch Data Analytics Of Original Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfTwitch)))


def barbasi():
    barabasiModelOfTwitchData = networkBuilder.generateBarabasiAlbertNetwork(vertices=list(originalNetworkOfTwitch.nodes), K=1000)
    print("Twitch Data Analytics Of Barbasi Graph : Average Path Length " + str(networkBuilder.computeAveragePathLength(barabasiModelOfTwitchData)))
    print("Twitch Data Analytics Of Barbasi Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(barabasiModelOfTwitchData)))


original()
barbasi()