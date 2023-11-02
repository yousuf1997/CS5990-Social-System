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
    twitchDataStatistic = [['Network Size', 'Average Degree', 'Average Path Length', 'Clustering Coefficient'],
                           [len(originalNetworkOfTwitch.edges),
                            networkBuilder.computeAverageDegree(originalNetworkOfTwitch),
                            networkBuilder.computeAveragePathLength(originalNetworkOfTwitch),
                            networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfTwitch)]]
    print("Twitch Data Analytics Of Original Graph")
    print(tabulate(twitchDataStatistic, headers='firstrow', tablefmt='fancy_grid'))


def barbasi():
    barabasiModelOfTwitchData = networkBuilder.generateBarabasiAlbertNetwork(vertices=list(originalNetworkOfTwitch.nodes), K=1000)
    barabasiModelOfTwitchDataStatistic = [['Average Path Length', 'Clustering Coefficient'],
                            [networkBuilder.computeAveragePathLength(barabasiModelOfTwitchData), networkBuilder.calculateAverageClusteringCoefficient(barabasiModelOfTwitchData)]]
    print("Barabasi Model Analytics Of Twitch Data")
    print(tabulate(barabasiModelOfTwitchDataStatistic, headers='firstrow', tablefmt='fancy_grid'))


original()
barbasi()