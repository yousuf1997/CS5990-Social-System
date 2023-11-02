import threading
from NetworkBuilder import NetworkBuilder
from DataReader import  DataReader
from tabulate import tabulate

networkBuilder = NetworkBuilder()
dataReader = DataReader()

'''
    The following two experiments,and constructs the graph of the network provided by the test data
'''

## the following code reads the amazon data
## construct the graph as per the edges in the data
originalNetworkOfAmazonRawData = dataReader.readData("Data/com-amazon.ungraph.txt", "Amazon")
originalNetworkOfAmazon = networkBuilder.buildGraph(originalNetworkOfAmazonRawData)


def original():
    print("Amazon Data Analytics Of Original Graph : Average Degree " + str(networkBuilder.computeAverageDegree(originalNetworkOfAmazon)))
    print("Amazon Data Analytics Of Original Graph : Average Path Length " + str(networkBuilder.computeAveragePathLength(originalNetworkOfAmazon)))
    print("Amazon Data Analytics Of Original Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfAmazon)))


def barbasi():
    barabasiModelOfAmazonData = networkBuilder.generateBarabasiAlbertNetwork(vertices=list(originalNetworkOfAmazon.nodes), K=1000)
    print("Amazon Data Analytics Of Barbasi Graph : Average Path Length " + str(networkBuilder.computeAveragePathLength(barabasiModelOfAmazonData)))
    print("Amazon Data Analytics Of Barbasi Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(barabasiModelOfAmazonData)))


original()
barbasi()

print("Amazon Data Analytics Of Original Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfAmazon)))
