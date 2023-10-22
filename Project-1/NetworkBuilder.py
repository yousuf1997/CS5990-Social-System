from hvplot import networkx
from networkx import Graph
import networkx as nx
import DataEdge
class NetworkBuilder:
    def __init__(self):
        pass

    def buildGraph(self, adjacencyList:list[DataEdge.DataEdge]) -> Graph:
        print("Building network...")
        network = Graph()
        for index in range(len(adjacencyList)):
             network.add_edge(adjacencyList[index].getVertex(), adjacencyList[index].getEdge())
        print("Finished building network...")
        return network

    def computeAverageDegree(self, graph:Graph) -> float:
        print("Computing average degree of the network")
        totalNodes = len(graph.nodes)
        totalDegree = 0
        for vertex, edges in graph.adj.items():
            for edge, weight in edges.items():
                totalDegree = totalDegree + 1
        print("Finished computing average degree of the network")
        return (totalDegree / totalNodes)

    def computeNetworkSize(self, graph:Graph) -> int:
        return graph.size()

    def computeAveragePathLength(self, graph: Graph) -> float:
        totalPathDistanceSum = 0
        totalPathSum = 0
        for vertex, edges in graph.adj.items():
            for otherVertex, innerEdges in graph.adj.items():
                if otherVertex != vertex:
                    print("Combination >> " + vertex + ", " + otherVertex)
                    try:
                        totalPathDistanceSum = totalPathDistanceSum + int(nx.shortest_path_length(graph, vertex, otherVertex, method='dijkstra'))
                        totalPathSum = totalPathSum + 1
                    except:
                        print("NetworkBuilder.computeAveragePathLength >> Exception thrown ")
        return totalPathDistanceSum / totalPathSum

    def generateWattsStrogatzNetwork(self, graph: Graph):
        pass