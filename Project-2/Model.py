
class Matrix:
    def __init__(self, name):
        self.matrix = {}
        self.__vertexList = set()
        self.name = name

    def put(self, vertex, edge):
        try:
            edgesMap = self.matrix[vertex]
        except:
            edgesMap = {}
        ## distance
        edgesMap[edge] = 0
        self.__vertexList.add(vertex)
        self.__vertexList.add(edge)
        self.matrix[vertex] = edgesMap

    def getEdges(self, vertex):
        try:
            return self.matrix[vertex]
        except Exception as e:
            return None

    def getVertex(self):
        return set(self.__vertexList)

    def getMatrix(self):
        return self.matrix

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

    def getEdgesWithWeight(self, vertex):
        edges = {}
        for matrix in self.__matrixContainer:
            try:
                mEdges = matrix.matrix[vertex]
                if mEdges != None:
                    for edge, distance in mEdges.items():
                        if not self.__isPresent(edges, edge):
                            edges[edge] = distance
            except:
                pass
        return edges

    def __isPresent(self, edges, edge):
        return edge in edges.keys()

    def updateDistanceToAnEdge(self, vertex, edge, distance):
        incrementer = 0
        while incrementer != -1 and incrementer < len(self.__matrixContainer):
            try:
                edgesMap = self.__matrixContainer[incrementer].matrix[vertex]
                edgesMap[edge] = distance
                self.__matrixContainer[incrementer][vertex] = edgesMap
                incrementer = -1
            except:
                pass
            incrementer = incrementer + 1

    def getVertex(self):
        vertex = []
        for matrix in self.__matrixContainer:
            vertex.extend(list(matrix.getVertex()))
        return sorted(set(vertex))

class ProcessorWrapper:
    def __init__(self, matrix: Matrix = None, scatterType: str = None, matrixWrapper : MatrixWrapper = None, vertex = None, subVertexIndexStart = None):
        self.scatterType = scatterType
        self.matrix = matrix
        self.matrixWrapper = matrixWrapper
        self.vertex = vertex
        self.subVertexIndexStart = subVertexIndexStart
        self.centralityInfo = {}
        self.allMatrixWrapper = []
        self.centralityMeasures = {}

    def getDistance(self, vertex, edges):
        index = 0
        while index < len(self.allMatrixWrapper):
            try:
                if self.allMatrixWrapper[index] != None:
                    if self.allMatrixWrapper[index].getEdgesWithWeight(vertex)[edges] is not None and \
                            self.allMatrixWrapper[index].getEdgesWithWeight(vertex)[edges] != 0:
                        return self.allMatrixWrapper[index].getEdgesWithWeight(vertex)[edges]
            except:
                pass
            index = index + 1
        return 0

