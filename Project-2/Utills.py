from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    visitedNodes = {}
    return dfs(adjacencyData, vertex, targetNode, visitedNodes)


import sys

def dfs(matrixWrapper, vertex, targetNode, visitedNodes):
    # Initialize visitedNodes if not done already
    if visitedNodes is None:
        visitedNodes = {}

    # Base case: Check if the current vertex is the target node
    if vertex == targetNode:
        return 0

    # Mark the current node as visited
    visitedNodes[vertex] = True

    # Get all edges of the vertex
    edges = matrixWrapper.getEdges(vertex)

    minPath = sys.maxsize

    for edge in edges:
        # Check if the edge is not visited
        if edge not in visitedNodes or not visitedNodes[edge]:
            # Recursively find the path length
            minPath = min(1 + dfs(matrixWrapper, edge, targetNode, visitedNodes), minPath)

    return minPath if minPath < sys.maxsize else sys.maxsize - 50  # Return -1 for unreachable targetNode
