from mpi4py import MPI
from Model import Matrix, MatrixWrapper, ProcessorWrapper
from DataReader import  DataReader
from Utills import compute_shortest_path

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dataReader = DataReader()

## scatter typoe
BUILD_ADJACENCY_LIST = "BUILT_ADJACENCY_LIST"
COMPUTE_SHORTEST_DISTANCE = "COMPUTE_SHORTEST_DISTANCE"

matrix = None

if rank == 0:
    ## populate empty matrix
    matrix = []
    for i in range(21):
        matrix.append(ProcessorWrapper(Matrix("rank " + str(i)), BUILD_ADJACENCY_LIST))
    ## if this is rank 0, it will send the data
    ## otherwise will receieve the data

comm.Barrier()

matrix = comm.scatter(matrix, root=0)


if matrix.scatterType == BUILD_ADJACENCY_LIST:
    if rank in range(0, 21):
        ## read the file and populate the individual matrix
        dataReader.readData("Data/twitter/twitter_combined" + str(rank) + ".txt", "Twitter", matrix.matrix)
    else:
        print("excessive ")

gatheredMatrix = comm.gather(matrix, root=0)

comm.Barrier()

if rank == 0:
    gatheredMatrix = list(gatheredMatrix)
    matrixWrapper = MatrixWrapper()
    for matrix in gatheredMatrix:
        if matrix.matrix.name != "rank 0":
            matrixWrapper.appendMatrix(matrix.matrix)
    print("Vertexes ", len(matrixWrapper.getVertex()))
    ### new scatter
    if gatheredMatrix[0].scatterType == BUILD_ADJACENCY_LIST:
        originalArray = matrixWrapper.getVertex()
        subarraySize = len(originalArray) // 20
        subVertex = [originalArray[i * subarraySize: (i + 1) * subarraySize] for i in range(20)]
        matrix = [ProcessorWrapper(None, COMPUTE_SHORTEST_DISTANCE)]
        for i, subV in enumerate(subVertex):
            subStartIndex = i
            if subStartIndex > 0:
                subStartIndex = (i * len(subVertex[0]))
            matrix.append(ProcessorWrapper(None, COMPUTE_SHORTEST_DISTANCE, matrixWrapper, subV, subStartIndex))

matrix = comm.scatter(matrix, root=0)

comm.Barrier()

if matrix.vertex != None:
    ## perform shortest path calculation
    subVertex = matrix.vertex ## sub vertex
    for index, vertex in enumerate(subVertex):
        ## compute the distance of each vertext
        for targetVertex in matrix.matrixWrapper.getVertex()[matrix.subVertexIndexStart:]:
            minDistance = compute_shortest_path(matrix.matrixWrapper, vertex, targetVertex)
            matrix.matrixWrapper.updateDistanceToAnEdge(vertex, targetVertex, minDistance)

gatheredMatrix = comm.gather(matrix, root=0)

comm.Barrier()

if rank == 0:
    gatheredMatrix = list(gatheredMatrix)
    print("Computed the shortest distances on each vertex")
    finalProcessWrapper = ProcessorWrapper()
    for processWrapper in gatheredMatrix:
        if processWrapper.matrixWrapper != None:
            ## print(str(processWrapper) + " Gathered >> A", processWrapper.matrixWrapper.getEdgesWithWeight("A"))
            finalProcessWrapper.allMatrixWrapper.append(processWrapper.matrixWrapper)

    originalArray = gatheredMatrix[1].matrixWrapper.getVertex()
    subarraySize = len(originalArray) // 20
    subVertex = [originalArray[i * subarraySize: (i + 1) * subarraySize] for i in range(20)]
    matrix = [(finalProcessWrapper, [])]
    for subV in subVertex:
        ## since this is undirected node
        ## in order to compute the centrality we need to find the distance of each vertex from the vertex
        matrix.append((finalProcessWrapper, subV))

matrix = comm.scatter(matrix, root=0)

comm.Barrier()


if rank > 0:
    ## compute the centrality
    ## for each vertex which is the second element of the tuple
    subVertexes = matrix[1]
    fProcessorWrapper = matrix[0]
    for vertex in subVertexes:
        sum = 0
        for edge in subVertexes:
            if vertex != edge:
                if fProcessorWrapper.getDistance(vertex, edge) != 0:
                    sum = sum + fProcessorWrapper.getDistance(vertex, edge)
                else:
                    sum = sum + fProcessorWrapper.getDistance(edge, vertex)
        fProcessorWrapper.centralityMeasures[vertex] = (len(fProcessorWrapper.allMatrixWrapper[1].getVertex()) - 1) / sum



gatheredCentrality = comm.gather(matrix, root=0)

comm.Barrier()


if rank == 0:
    print("Finsihed calcualting centrality measures")
    gatheredCentrality = list(gatheredCentrality)
    for c in gatheredCentrality:
        print("centralityMeasures " , c[0].centralityMeasures)