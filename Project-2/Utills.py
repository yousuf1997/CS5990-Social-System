from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    visitedNodes = {}
    return dfs(adjacencyData, vertex, targetNode, visitedNodes)


def dfs(matrixWrapper, vertex, targetNode, visitedNodes):
    if vertex == targetNode:
        return sys.maxsize - 50

    # Mark the current node as visited
    visitedNodes[vertex] = True

    # Get all edges of the vertex
    edges = matrixWrapper.getEdges(vertex)

    minPath = sys.maxsize - 50

    for edge in edges:
        if edge not in visitedNodes or not visitedNodes[edge]:
            minPath = min(1 + dfs(matrixWrapper, edge, targetNode, visitedNodes), minPath)

    return minPath