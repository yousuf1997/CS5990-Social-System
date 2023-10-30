import random

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
        counter = 0
        for vertex, edges in graph.adj.items():
            counter = counter + 1
            for edge, weight in edges.items():
                totalDegree = totalDegree + 1
            # print("computeAverageDegree >> " + str(counter))
        print("Finished computing average degree of the network")
        return (totalDegree / totalNodes)

    def computeNetworkSize(self, graph:Graph) -> int:
        return graph.size()

    def computeAveragePathLength(self, graph: Graph) -> float:
        print("Computing average path length")
        totalPathDistanceSum = 0
        totalPathSum = 0
        counter = 0
        for vertex, edges in graph.adj.items():
            counter = counter + 1
            for otherVertex, innerEdges in graph.adj.items():
                if otherVertex != vertex:
                    try:
                        totalPathDistanceSum = totalPathDistanceSum + int(nx.shortest_path_length(graph, vertex, otherVertex, method='dijkstra'))
                        totalPathSum = totalPathSum + 1
                    except:
                        print("NetworkBuilder.computeAveragePathLength >> Exception thrown ")
            # print("computeAveragePathLength >> " + str(counter))
        print("Finished computing average path length")
        return totalPathDistanceSum / totalPathSum

    def generateBarabasiAlbertNetwork(self, vertices:list, K:int) -> Graph:
        '''
          1) First build the base network and make sure that each
             node have at least one edge and compute probabilities on the way
        '''
        print("Starting to build Barabasi Albert Network")
        barabasiAlbertNetwork = Graph()
        probabilitiesOfNodes = [] ## list of tuples (vertex, probability)

        ## generate K nodes (initial network) and create at least one edge on nodes
        randomIndex = random.randrange(0, len(vertices))
        barabasiAlbertNetwork.add_node(vertices[randomIndex])
        ## remove the vertex from the vertices
        previouslyAddedVertex = vertices[randomIndex]
        vertices.remove(vertices[randomIndex])
        counter = K - 1

        while counter > 0:
            randomIndex = random.randrange(0, len(vertices))
            ## join edge the randomly selected node to the previously added vertex
            barabasiAlbertNetwork.add_edge(previouslyAddedVertex, vertices[randomIndex])
            previouslyAddedVertex = vertices[randomIndex]
            vertices.remove(vertices[randomIndex])
            counter = counter - 1

        ## count the probabilities of the current networks nodes
        for node in barabasiAlbertNetwork.nodes:
            self._calculateProbability(graph=barabasiAlbertNetwork, probabilitiesOfNode=probabilitiesOfNodes,
                                       vertex=node)
        print("Finished building base network")
        ## iterate through the rest of the avaiable vertex
        counter = 0
        for node in vertices:
            ## pick the random one from the probability
            selected_node_as_edge, probability = random.choices(probabilitiesOfNodes, k=1)[0]
            counter = counter + 1
            # print("counter >> " + str(counter))
            ## connect new node to the selected edge
            barabasiAlbertNetwork.add_edge(selected_node_as_edge, node)
            ## re calculate probability for both vertex and edge
            ## edge
            self._calculateProbability(graph=barabasiAlbertNetwork, probabilitiesOfNode=probabilitiesOfNodes,
                                       vertex=selected_node_as_edge)
            ## current vetex
            self._calculateProbability(graph=barabasiAlbertNetwork, probabilitiesOfNode=probabilitiesOfNodes,
                                       vertex=node)
        print("Finished building Barabasi Albert Network")
        return barabasiAlbertNetwork

    def _calculateProbability(self, graph:Graph, probabilitiesOfNode: list, vertex:any):
        newProbability = (vertex, graph.degree(vertex) / (2 * graph.number_of_edges()))
        newProbabilityTuple = (vertex, newProbability)
        ## check the is if the combination is already present
        for listVertex, probability in probabilitiesOfNode:
            if vertex == listVertex:
                ## found the combination and remove
                probabilitiesOfNode.remove((listVertex, probability))
                break
        ## add the new probability
        probabilitiesOfNode.append(newProbabilityTuple)

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
            # print("Removed edges >> V = " + str(totalNodesOfGraphList[randomVertexIndex]) + " , E = " + totalNodesOfGraphList[randomTerminateEdgeIndex])
            ## now lets pick another random vertex
            targetRandomVertexIndex = random.randrange(0, len(totalNodesOfGraphList))
            ## rewire will be done in the following
            rewireDone = False
            while (rewireDone != True):
                try:
                    ## check the if the vertext has already connection with the randomly targeted node
                    ## if there is, then compute another random vertex
                    if (regularRingLatticeGraph.has_edge(totalNodesOfGraphList[randomVertexIndex], totalNodesOfGraphList[targetRandomVertexIndex]) or randomVertexIndex == targetRandomVertexIndex):
                        ## since there is already an edge between the vertex and the random vertext
                        ## compute another random
                        targetRandomVertexIndex = random.randrange(0, len(totalNodesOfGraphList))
                    else:
                        ## since we do not have an edge
                        ## we will rewire the vertex to the random vertex
                        regularRingLatticeGraph.add_edge(totalNodesOfGraphList[randomVertexIndex],
                                                         totalNodesOfGraphList[targetRandomVertexIndex])
                        rewireDone = True
                        # print("Rewired edges >> V = " + str(totalNodesOfGraphList[randomVertexIndex]) + " , E = " + totalNodesOfGraphList[targetRandomVertexIndex])
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

    def calculateAverageClusteringCoefficient(self, graph:Graph) -> float:
        totalNodes = len(graph.nodes)
        clusteringCoefficientTotal = nx.clustering(graph)
        totalCoefficient = 0
        print("Computing clustering coefficient")
        for vertex, coefficient in clusteringCoefficientTotal.items():
            totalCoefficient = totalCoefficient + coefficient
        print("Finished computing clustering coefficient")
        return totalCoefficient / totalNodes