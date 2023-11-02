import threading
from NetworkBuilder import NetworkBuilder
from DataReader import  DataReader
from tabulate import tabulate

networkBuilder = NetworkBuilder()
dataReader = DataReader()

'''
    srun -n 1 --ntasks-per-node=1 -p gpu -J amazonW --priority="TOP" -u python AmazonWatts.py > amazonWatts.txt
'''

## the following code reads the amazon data
## construct the graph as per the edges in the data
originalNetworkOfAmazonRawData = dataReader.readData("Data/com-amazon.ungraph.txt", "Amazon")
originalNetworkOfAmazon = networkBuilder.buildGraph(originalNetworkOfAmazonRawData)


def watts():
    amazonModelOfTwitchData = networkBuilder.generateWattsStrogatzNetwork(originalNetworkOfAmazon, K=200, beta=0.001)
    print("Amazon Data Analytics Of Watts Graph : Average Path Length " + str(networkBuilder.computeAveragePathLength(amazonModelOfTwitchData)))
    print("Amazon Data Analytics Of Watts Graph : Average Clustering " + str(networkBuilder.calculateAverageClusteringCoefficient(amazonModelOfTwitchData)))


watts()
