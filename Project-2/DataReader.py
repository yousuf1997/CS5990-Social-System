## Reader class reads data to contruct graph, and it returns edges as list
import DataEdge
class DataReader:
    def __init__(self):
        pass

    def readData(self, filePath, dataType):
        if (filePath == None or filePath == ' '):
            return None
        ## open the file
        file = open(filePath, "r")
        ## all the lines as a graph
        adjacencyMap = {}
        lines = file.readlines()
        for index, line in enumerate(lines):
            lineData = line.split(' ')
            ## vertex, edge
            try:
                edgeList = adjacencyMap[str(lineData[0].strip())]
                edgeList.append(str(lineData[1].strip()))
                adjacencyMap[str(lineData[0].strip())] = edgeList
            except:
                adjacencyMap[str(lineData[0].strip())] = [str(lineData[1].strip())]
        print("Finished reading data from " + filePath + " >> " + dataType + " data set")
        return adjacencyMap