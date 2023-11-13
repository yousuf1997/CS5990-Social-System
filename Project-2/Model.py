
class Matrix:
    def __init__(self, name):
        self.__matrix = {}
        self.__vertexList = set()
        self.name = name

    def put(self, vertex, edge):
        edgesMap = {}
        try:
            edgesMap = self.__matrix[vertex]
        except:
            pass
        ## distance
        edgesMap[edge] = 0

        self.__vertexList.add(vertex)
        self.__vertexList.add(edge)

        self.__matrix[vertex] = edgesMap

    def getEdges(self, vertex):
        try:
            return list(self.__matrix[vertex].keys())
        except:
            return None

    def getVertex(self):
        return set(self.__vertexList)

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
            mEdges = matrix.getEdges(vertex)
            if mEdges != None:
                edges.extend(mEdges)
        return sorted(list(set(edges)))

    def updateDistanceToAnEdge(self, vertex, edge, distance):
        edgeMap = None
        try:
            edgeMap = self.__matrixContainer[vertex]
        except:
            self.__matrixContainer[vertex] = {}
            edgeMap = self.__matrixContainer[vertex]
        edgeMap[edge] = distance

    def getVertex(self):
        vertex = []
        for matrix in self.__matrixContainer:
            vertex.extend(list(matrix.getVertex()))
        return sorted(set(vertex))

class ProcessorWrapper:
    def __init__(self, matrix: Matrix, scatterType: str, marixWrapper : MatrixWrapper = None, vertex = None):
        self.scatterType = scatterType
        self.matrix = matrix
        self.matrixWrapper = marixWrapper
        self.vertex = vertex
