
class Matrix:
    def __init__(self, name):
        self.__matrix = {}
        self.name = name

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
        try:
            return list(self.__matrix[vertex].keys())
        except:
            return None

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
            print("Reading ", matrix)
            mEdges = matrix.getEdges(vertex)
            if mEdges != None:
                edges.extend(mEdges)
        return list(set(edges))
