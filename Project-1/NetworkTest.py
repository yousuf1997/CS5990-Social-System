'''
    Experimenting the Watts-Strogatz, Barabasi-Albert
'''
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
# amazonDataStatistic = [['Network Size', 'Average Degree', 'Average Path Length', 'Clustering Coefficient'],
#                         [len(originalNetworkOfAmazon.edges), networkBuilder.computeAverageDegree(originalNetworkOfAmazon),
#                          networkBuilder.computeAveragePathLength(originalNetworkOfAmazon), networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfAmazon)]]
# print("Amazon Data Analytics Of Original Graph")
# print(tabulate(amazonDataStatistic, headers='firstrow', tablefmt='fancy_grid'))

#
# ## the following code reads the twitch data
# ## construct the graph as per the edges in the data
# originalNetworkOfTwitchRawData = dataReader.readData("[YOUR_PATH]//arge twitch_edges.csv", "Twitch")
# originalNetworkOfTwitch = networkBuilder.buildGraph(originalNetworkOfAmazonRawData)
# twitchDataStatistic = [['Network Size', 'Average Degree', 'Average Path Length', 'Clustering Coefficient'],
#                         [len(originalNetworkOfTwitch.edges), networkBuilder.computeAverageDegree(originalNetworkOfTwitch),
#                          networkBuilder.computeAveragePathLength(originalNetworkOfTwitch), networkBuilder.calculateAverageClusteringCoefficient(originalNetworkOfTwitch)]]
# print("Twitch Data Analytics Of Original Graph")
# print(tabulate(twitchDataStatistic, headers='firstrow', tablefmt='fancy_grid'))
#
# '''
#     The following two experiments, construct the Watts-Strogatz, and Barabasi-Albert model based on the nodes of the test data.
#     Since we arleady read the data, we do not need to read it again.
# '''
#
# wattsStrogarzModelOfAmazonData = networkBuilder.generateWattsStrogatzNetwork(graph=originalNetworkOfAmazon, K=120, beta=0.01)
# wattsStrogarzModelOfAmazonDataStatistic = [['Average Path Length', 'Clustering Coefficient'],
#                         [networkBuilder.computeAveragePathLength(wattsStrogarzModelOfAmazonData), networkBuilder.calculateAverageClusteringCoefficient(wattsStrogarzModelOfAmazonData)]]
# print("Watts-Strogatz Mode Analytics Of Amazon Data")
# print(tabulate(wattsStrogarzModelOfAmazonDataStatistic, headers='firstrow', tablefmt='fancy_grid'))
#
barabasiModelOfAmazonData = networkBuilder.generateBarabasiAlbertNetwork(graph=originalNetworkOfAmazon, K=1000)
barabasiModelOfAmazonDataAmazonDataStatistic = [['Average Path Length', 'Clustering Coefficient'],
                        [networkBuilder.computeAveragePathLength(barabasiModelOfAmazonData), networkBuilder.calculateAverageClusteringCoefficient(barabasiModelOfAmazonData)]]
print("Barabasi Mode Analytics Of Amazon Data")
print(tabulate(barabasiModelOfAmazonDataAmazonDataStatistic, headers='firstrow', tablefmt='fancy_grid'))
#
#
# wattsStrogarzModelOfTwitchData = networkBuilder.generateWattsStrogatzNetwork(graph=originalNetworkOfTwitch, K=120, beta=0.01)
# wattsStrogarzModelOfTwitchDataStatistic = [['Average Path Length', 'Clustering Coefficient'],
#                         [networkBuilder.computeAveragePathLength(wattsStrogarzModelOfTwitchData), networkBuilder.calculateAverageClusteringCoefficient(wattsStrogarzModelOfTwitchData)]]
# print("Watts-Strogatz Mode Analytics Of Twitch Data")
# print(tabulate(wattsStrogarzModelOfTwitchDataStatistic, headers='firstrow', tablefmt='fancy_grid'))
#
# barabasiModelOfTwitchData = networkBuilder.generateBarabasiAlbertNetwork(graph=originalNetworkOfTwitch, K=1000)
# barabasiModelOfTwitchDataStatistic = [['Average Path Length', 'Clustering Coefficient'],
#                         [networkBuilder.computeAveragePathLength(barabasiModelOfTwitchData), networkBuilder.calculateAverageClusteringCoefficient(barabasiModelOfTwitchData)]]
# print("Barabasi Mode Analytics Of Amazon Data")
# print(tabulate(barabasiModelOfTwitchDataStatistic, headers='firstrow', tablefmt='fancy_grid'))
