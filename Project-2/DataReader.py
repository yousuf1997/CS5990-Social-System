## Reader class reads data to contruct graph, and it returns edges as list
import DataEdge
from Model import Matrix
class DataReader:
    def __init__(self):
        pass

    def readData(self, filePath, dataType) -> Matrix:
        if (filePath == None or filePath == ' '):
            return None
        ## open the file
        file = open(filePath, "r")
        ## all the lines as a graph
        lines = file.readlines()
        ## result
        matrix = Matrix()
        for index, line in enumerate(lines):
                    lineData =  line.split('\t')
                    ## vertex, edge
                    matrix.put(lineData[0].strip(), lineData[1].strip())
        print("Finished reading data from " + dataType + " data set")
        return matrix