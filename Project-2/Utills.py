
class AdjacencyList:

    def __init__(self):
        self.__adjacencyMap = {}

    def append(self, vertex, edge):
        try:
            self.__adjacencyMap[vertex].append(edge)
        except:
            ## key does not exists create new one
            self.__adjacencyMap[vertex] = [edge]

    def getEdges(self, vertex):
        return self.__adjacencyMap[vertex]

    def printAdjacencyList(self):
        for vertex, edges in self.__adjacencyMap.items():
            print("Vertex >> " + vertex, "edges >> ", edges)