import random

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

    def generateWattsStrogatzNetwork(self, graph: Graph, K: int, beta: float) -> Graph:
        '''
            -- Algorithm step 1 --
            Generate regular ring lattice
            -- Algorithm step 2 --
            we wil extract the total nodes as a list
            we will use that nodes to pick random vertex at time
            from that vertext, we pick random edge from the edges of the vertex
            then we cutt of the connection between the edge and the vertex
            then we randomly pick another vertex from the total nodes
            we check if already connection exists between then, if not then we connect the vertexes,
            otherwise we pick another from the total number of nodes
         '''
        ## build the ring lattice from the graph
        regularRingLatticeGraph = self.generatRegularRingLatticeGraph(graph, K)
        ## beta times the total edges of the graph
        totalNodesToBeRewiredRandomly = int(regularRingLatticeGraph.size() * beta)
        totalNodesOfGraphList = self.getAllNodesFromGraph(regularRingLatticeGraph)
        print("Regular Ring lattice network has total of " + str(regularRingLatticeGraph.size()) + " Edges.")
        print("We will be rewiring total of " + str(totalNodesToBeRewiredRandomly) + " edges.")
        for vertex in range(totalNodesToBeRewiredRandomly):
            ## pick random vertex
            ## pick random edge of the vertex
            ## cutt off the connection
            randomVertexIndex = random.randrange(0, len(totalNodesOfGraphList))
            vertexEdges = self._getEdgesOfVertexAsAList(regularRingLatticeGraph, totalNodesOfGraphList[randomVertexIndex])
            randomTerminateEdgeIndex = random.randrange(0, len(vertexEdges))
            ## terminate the connection of the vertext and edge
            regularRingLatticeGraph.remove_edge(totalNodesOfGraphList[randomVertexIndex], vertexEdges[randomTerminateEdgeIndex])
            print("Removed edges >> V = " + str(totalNodesOfGraphList[randomVertexIndex]) + " , E = " + totalNodesOfGraphList[randomTerminateEdgeIndex])
            ## now lets pick another random vertex
            targetRandomVertexIndex = random.randrange(0, len(totalNodesOfGraphList))
            ## rewire will be done in the following
            rewireDone = False
            while (rewireDone != True):
                try:
                    ## check the if the vertext has already connection with the randomly targeted node
                    ## if there is, then compute another random vertex
                    if (regularRingLatticeGraph.has_edge(totalNodesOfGraphList[randomVertexIndex], totalNodesOfGraphList[targetRandomVertexIndex])):
                        ## since there is already an edge between the vertex and the random vertext
                        ## compute another random
                        targetRandomVertexIndex = random.randrange(0, len(totalNodesOfGraphList))
                    else:
                        ## since we do not have an edge
                        ## we will rewire the vertex to the random vertex
                        regularRingLatticeGraph.add_edge(totalNodesOfGraphList[randomVertexIndex],
                                                         totalNodesOfGraphList[targetRandomVertexIndex])
                        rewireDone = True
                        print("Rewired edges >> V = " + str(totalNodesOfGraphList[randomVertexIndex]) + " , E = " + totalNodesOfGraphList[targetRandomVertexIndex])
                except:
                    targetRandomVertexIndex = random.randrange(0, len(totalNodesOfGraphList))
                    # rewireDone = True
        return regularRingLatticeGraph

    def generatRegularRingLatticeGraph(self, graph: Graph, K: int) -> Graph:
        regularRingLatticeGraph = Graph()
        sortedNodeList = self.getAllNodesFromGraph(graph)
        nodeListLength = len(sortedNodeList)
        for vertexIndex in range(nodeListLength):
            for edgeIndex in range(int(K / 2)):
                targetNodeIndex = self._getIndex(vertexIndex + edgeIndex + 1, nodeListLength)
                regularRingLatticeGraph.add_edge(sortedNodeList[vertexIndex], sortedNodeList[targetNodeIndex])
        return regularRingLatticeGraph

    def getAllNodesFromGraph(self, graph : Graph) -> list:
        return sorted(graph.nodes)

    def _getIndex(self, targetedIndex: int, listLength: int) -> int:
        if (targetedIndex < listLength):
            return targetedIndex
        return abs(targetedIndex - listLength)

    def _getEdgesOfVertexAsAList(self, graph:Graph, vertex) -> list:
        ## get the addjaceny list of the graph per vertex
        adjacenyItem = graph.adj[vertex]
        listOfEdges = []
        for edge, weight in adjacenyItem.items():
            listOfEdges.append(edge)
        return listOfEdges