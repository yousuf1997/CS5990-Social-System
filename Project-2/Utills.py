from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    visitedNodes = {}
    return dfs(adjacencyData, vertex, targetNode, visitedNodes, 0, sys.maxsize - 50)

def dfs(matrixWrapper, vertex, targetNode, visitedNodes, count, minPath):
    # Base case: Check if the current vertex is the target node
    if vertex == targetNode:
        return count

    if count > minPath:
        return count
    
    # Mark the current node as visited
    visitedNodes.add(vertex)
    count += 1

    # Get all edges of the vertex
    edges = matrixWrapper.getEdges(vertex)

    for edge in edges:
        # Check if the edge is not visited
        if edge not in visitedNodes:
            # Recursively find the path length
            new_count = dfs(matrixWrapper, edge, targetNode, visitedNodes, count, minPath)
            # Update minPath if a shorter path is found
            minPath = min(new_count, minPath)

    return minPath
