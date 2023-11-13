from Model import MatrixWrapper
import sys
def compute_shortest_path(adjacencyData : MatrixWrapper, vertex, targetNode) -> int:
    visitedNodes = set()
    return bfs(adjacencyData, vertex, targetNode)

def bfs(matrixWrapper, vertex, targetNode):
    # Base case: Check if the current vertex is the target node
    visitedNodes = set()

    queue = []

    queue.append([vertex, 1])
    visitedNodes.add(vertex)
    minPath = sys.maxsize - 50

    while queue:
        current = queue.pop()
        edges = matrixWrapper.getEdges(current[0])
        if current[0] == targetNode:
            return current[1] - 1
        for edge in edges:
            if edge not in visitedNodes:
                visitedNodes.add(edge)
                queue.append([edge, current[1] + 1])

    return minPath