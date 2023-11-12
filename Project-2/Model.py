

class Matrix:
    def __init__(self):
        self.__matrix = {}

    def put(self, vertex, edge):
        edgesMap = {}
        try:
            edgesMap = self.__matrix[vertex]
        except:
            pass
        ## distance
        edgesMap[edge] = 0
        self.__matrix[vertex] = edgesMap

    def getEdges(self, vertex):
        return self.__matrix[vertex].keys()

