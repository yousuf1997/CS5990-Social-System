## Reader class reads data to contruct graph, and it returns edges as list
import DataEdge
from Model import Matrix
class DataReader:
    def __init__(self):
        pass

    def readData(self, filePath, dataType, matrix: Matrix):
        if (filePath == None or filePath == ' '):
            return None
        ## open the file
        file = open(filePath, "r")
        ## all the lines as a graph
        lines = file.readlines()
        for index, line in enumerate(lines):
            lineData = line.split(' ')
            ## vertex, edge
            matrix.put(str(lineData[0].strip()), (str(lineData[1].strip()) if len(lineData) > 1 else str(-1)))
        print("Finished reading data from " + filePath + " >> " + dataType + " data set")