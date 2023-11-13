
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
        return list(self.__matrix[vertex].keys())

    def getMatrix(self):
        return self.__matrix

class MatrixWrapper:

    def __init__(self):
        self.__matrixContainer = []

    def appendMatrix(self, matrix:Matrix):
        self.__matrixContainer.append(matrix)

    def getEdges(self, vertex):
        edges = []
        for matrix in self.__matrixContainer:
            edges.extend(matrix.getEdges(vertex))
        return list(set(edges))
