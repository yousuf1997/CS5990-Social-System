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
    amazonDataStatistic = [['Network Size', 'Average Degree', 'Average Path Length', 'Clustering Coefficient'],
                           [len(originalNetworkOfAmazon.edges),
                            networkBuilder.computeAverageDegree(originalNetworkOfAmazon),
                            networkBuilder.computeAveragePathLength(originalNetworkOfAmazon),
                            networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfAmazon)]]
    print("Amazon Data Analytics Of Original Graph")
    print(tabulate(amazonDataStatistic, headers='firstrow', tablefmt='fancy_grid'))


def barbasi():
    barabasiModelOfAmazonData = networkBuilder.generateBarabasiAlbertNetwork(vertices=list(originalNetworkOfAmazon.nodes), K=1000)
    barabasiModelOfAmazonDataAmazonDataStatistic = [['Average Path Length', 'Clustering Coefficient'],
                            [networkBuilder.computeAveragePathLength(barabasiModelOfAmazonData), networkBuilder.calculateAverageClusteringCoefficient(barabasiModelOfAmazonData)]]
    print("Barabasi Mode Analytics Of Amazon Data")
    print(tabulate(barabasiModelOfAmazonDataAmazonDataStatistic, headers='firstrow', tablefmt='fancy_grid'))


originalAmazon = threading.Thread(target=original)
originalAmazon.start()

barbasiAmazon = threading.Thread(target=barbasi)
barbasiAmazon.start()