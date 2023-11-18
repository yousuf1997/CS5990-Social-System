from networkx import Graph
import networkx as nx
from DataReader import  DataReader
from mpi4py import MPI
import Model as m

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dataReader = DataReader()


## read the data from across the stream
adjacencyMap = None

if rank == 0:
    adjacencyMap = []
    for i in range(5):
        adjacencyMap.append({})

comm.Barrier()

adjacencyMap = comm.scatter(adjacencyMap, root=0)

## read the data and append to the current instance of the dictionary
adjacencyMap.update(dataReader.readData("Data/twitter/twitter_combined_" + str(rank) + ".txt", "Facebook"))

aggregatedAdjacencyMap = comm.gather(adjacencyMap, root=0)

comm.Barrier()


## the following section will aggregate the list and build the Graph
graphSubVertexData = []

if rank == 0:
    print("We are the merging stage, received total of", len(aggregatedAdjacencyMap) - 1, "data.")
    aggregateGraph = nx.DiGraph()
    for adjMap in aggregatedAdjacencyMap:
        if len(adjMap) != 0:
            for vertex, edges in adjMap.items():
                for edge in edges:
                    aggregateGraph.add_edge(str(vertex), str(edge))
                    aggregateGraph.add_edge(str(edge), str(vertex))
    print("Aggregated the data, we have total of ", len(aggregateGraph.nodes), "nodes, and", len(aggregateGraph.edges), "edges")
    ## build sublist of vertex
    aggregateGraph = aggregateGraph.to_undirected()
    totalVertex = aggregateGraph.nodes
    subListLength = len(totalVertex) // 4
    totalSubList = 0
    subListStartIndex = 0
    graphSubVertexData.append(())
    while totalSubList < 4:
        graphSubVertexData.append((aggregateGraph, list(totalVertex), subListStartIndex, subListStartIndex + subListLength, []))
        subListStartIndex = subListStartIndex + subListLength
        totalSubList = totalSubList + 1


## scatter into different processor
comm.Barrier()

graphSubVertexData = comm.scatter(graphSubVertexData, root=0)

## here we calculate the shortest distance
calculateShortestDistances = {}

if rank > 0:
    graph = graphSubVertexData[0]
    allVertex = graphSubVertexData[1]
    vertexIndex = graphSubVertexData[2]
    endingIndex = graphSubVertexData[3]

    ## calculate shortest path distance for each vertex and edge
    while vertexIndex < len(allVertex) and vertexIndex <= endingIndex:
        edgeIndex = vertexIndex + 1
        while edgeIndex < len(allVertex):
            calculateShortestDistances[(allVertex[vertexIndex], allVertex[edgeIndex])] = nx.shortest_path_length(graph, allVertex[vertexIndex], allVertex[edgeIndex])
            edgeIndex = edgeIndex + 1
        vertexIndex = vertexIndex + 1

    graphSubVertexData[4].append(calculateShortestDistances)

## gather
aggregatedAdjacencyMap = comm.gather(graphSubVertexData, root=0)

comm.Barrier()

graphSubVertexData = []
if rank == 0:
    print("We are the merging stage of calculated shortest distance.")
    graphSubVertexData.append(())
    shortestDistanceData = {}
    for aMap in aggregatedAdjacencyMap:
        if len(aMap) > 0:
            shortestDistanceData.update(aMap[4][0])
    for aMap in aggregatedAdjacencyMap:
        if len(aMap) > 0:
            graphSubVertexData.append((aMap[0],aMap[1],aMap[2],aMap[3],aMap[4], {}))

comm.Barrier()
##
graphSubVertexData = comm.scatter(graphSubVertexData, root=0)

## here we calcualte the closeness centrality

if rank > 0:
    print("we are at the closeness centrality stage")
    ## total of nodes - 1 / sum(all shortest distance)
    graph = graphSubVertexData[0]
    allVertex = graphSubVertexData[1]
    vertexIndex = graphSubVertexData[2]
    endingIndex = graphSubVertexData[3]
    calculateShortestDistances = graphSubVertexData[4][0]

    ## calculate shortest path distance for each vertex and edge
    while vertexIndex < len(allVertex) and vertexIndex <= endingIndex:
        edgeIndex = vertexIndex + 1
        while edgeIndex < len(allVertex):
            graphSubVertexData[5][allVertex[vertexIndex]] = (len(allVertex) - 1) / m.getTheSumOfAllWeightsOfTheVertex(allVertex[vertexIndex],allVertex, calculateShortestDistances)
            edgeIndex = edgeIndex + 1
        vertexIndex = vertexIndex + 1

## gather
aggregatedAdjacencyMap = comm.gather(graphSubVertexData, root=0)

comm.Barrier()

graphSubVertexData = []
if rank == 0:
    aggregatedClosenessCentrality = {}
    print(f"ID  >> {rank} : We are the merging the aggregated closeness centrality")
    for adjMap in aggregatedAdjacencyMap:
        if len(adjMap) > 0:
            aggregatedClosenessCentrality.update(adjMap[5])
    # Sort the dictionary by values in ascending order
    sorted_items = sorted(aggregatedClosenessCentrality.items(), key=lambda item: item[1], reverse=True)

    print("Printing the top 5 items")
    for i, (key, value) in enumerate(sorted_items[:5], 1):
        print(f"{i}. Key: {key}, Value: {value}")
