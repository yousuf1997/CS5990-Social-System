## Model class representing data from data set
class DataEdge:
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge

    def getVertex(self):
        return self.vertex

    def getEdge(self):
        return self.edge
