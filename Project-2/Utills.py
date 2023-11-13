from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    visitedNodes = {}
    return dfs(adjacencyData, vertex, targetNode, visitedNodes)

def dfs(matrixWrapper : MatrixWrapper, vertex, targetNode, visitedNodes) -> int:
    if vertex == targetNode:
        return 0
    ## mark the current node as visited
    visitedNodes[vertex] = True
    ## get the all edges of the vertex
    edges = matrixWrapper.getEdges(vertex)
    minPath = sys.maxsize - 50
    for edge in edges:
        try:
            visted = visitedNodes[edge]
        except:
            minPath = min(1 + dfs(matrixWrapper, edge, targetNode, visitedNodes), minPath)
    return minPath