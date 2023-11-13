from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    visitedNodes = {}
    return dfs(adjacencyData, vertex, targetNode, visitedNodes, 0)

def dfs(matrixWrapper, vertex, targetNode, visitedNodes, count):
    # Base case: Check if the current vertex is the target node
    if vertex == targetNode:
        return count

    # Mark the current node as visited
    visitedNodes[vertex] = True
    count = count + 1
    # Get all edges of the vertex
    edges = matrixWrapper.getEdges(vertex)

    minPath = sys.maxsize - 50

    for edge in edges:
        # Check if the edge is not visited
        if edge not in visitedNodes.keys():
            # Recursively find the path length
            minPath = min(dfs(matrixWrapper, edge, targetNode, dict(visitedNodes), count), minPath)

    return minPath
