import threading

from networkx import Graph

from NetworkBuilder import NetworkBuilder
import networkx as nx
import matplotlib.pyplot as plt
import time
import concurrent.futures
import numpy
from multiprocessing import Pool
# Number of nodes and edges
num_nodes = 1000
num_edges = 10000  # You can adjust this number as needed

# Create a random graph with 50 nodes and 100 edges
G = nx.gnm_random_graph(num_nodes, num_edges, directed=False)

networkBuilder = NetworkBuilder()

#
# startTime = time.time()
# networkBuilder.computeAveragePathLength(G)
# endTime = time.time()





def vertexLevelThreadHelper(vertex, G:Graph, sumPathList:list):
    allNodes = list(G.nodes)
    index = 0
    length = len(allNodes)
    vertexLevelThreads = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        while index < length:
            subList = allNodes[index:index + 300]
            # newThread = threading.Thread(target=vertexPathComputeThreadHelper, args=(vertex, subList, G, sumPathList))
            # vertexLevelThreads.append(newThread)
            # newThread.start()
            ## vertexPathComputeThreadHelper(vertex, subList, G, sumPathList)
            future = executor.submit(vertexPathComputeThreadHelper, vertex, subList, G, sumPathList)
            index = index + 300
        ## executor.shutdown(wait=True)
    # ## join all the sub threads
    # for thread in vertexLevelThreads:
    #     thread.

def vertexPathComputeThreadHelper(vertex, sublist: list, G:Graph, sumPathList:list):
    sumLength = 0
    count = 0
    for edges in sublist:
        try:
            if vertex != edges:
                count = count + 1
                sumLength = sumLength + int(nx.shortest_path_length(G, vertex, edges, method='dijkstra'))
        except:
            pass
    sumPathList.append(float(sumLength / count))


def computeAveragePathLength(G:Graph):
    allNodes = list(G.nodes)
    baseThreads = []
    sumPathList = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        tup = []
        for vertex in allNodes:
            future = executor.submit(vertexLevelThreadHelper, vertex, G, sumPathList)

        # results = pool.starmap(vertexLevelThreadHelper, tuple(tup))
        ## executor.shutdown(wait=True)
    return sum(sumPathList) / len(sumPathList)


if __name__ == "__main__":
    startTime = time.time()
    value = nx.average_shortest_path_length(G)
    endTime = time.time()
    print("Without Thread ->> " + str(value) + " >> " + str(endTime - startTime))

    startTime = time.time()
    value = computeAveragePathLength(G)
    endTime = time.time()

    print("With Thread ->> " + str(value) + " >> " + str(endTime - startTime))


    startTime = time.time()
    value= networkBuilder.computeAveragePathLength(G)
    endTime = time.time()

    print("With Thread (networkBuilder) ->> " + str(value) + " >> " + str(endTime - startTime))