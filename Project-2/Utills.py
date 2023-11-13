from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    return bfs(adjacencyData, vertex, targetNode)

def bfs(matrixWrapper, vertex, targetNode):
    # Base case: Check if the current vertex is the target node
    visitedNodes = set()

    queue = []

    queue.append([vertex, 0])

    while queue:
        current = queue.pop(0)
        edges = matrixWrapper.getEdges(current[0])
        if current[0] == targetNode:
            return current[1]
        if current[0] not in visitedNodes:
            visitedNodes.add(current[0])
            for edge in edges:
                if edge not in visitedNodes:
                    queue.append([edge, current[1] + 1])
    return 0