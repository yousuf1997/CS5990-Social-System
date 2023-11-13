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
    for i in range(41):
        matrix.append(ProcessorWrapper(Matrix("rank " + str(i)), BUILD_ADJACENCY_LIST))
    ## if this is rank 0, it will send the data
    ## otherwise will receieve the data

comm.Barrier()

matrix = comm.scatter(matrix, root=0)


if matrix.scatterType == BUILD_ADJACENCY_LIST:
    if rank in range(0, 21):
        ## read the file and populate the individual matrix
        dataReader.readData("Data/twitter/twitter_combined_" + str(rank) + ".txt", "Twitter", matrix.matrix)
    else:
        pass
if matrix.scatterType == COMPUTE_SHORTEST_DISTANCE:
    print("Received sub vertex")


gatheredMatrix = comm.gather(matrix, root=0)

comm.Barrier()

if rank == 0:
    gatheredMatrix = list(gatheredMatrix)
    matrixWrapper = MatrixWrapper()
    for matrix in gatheredMatrix:
        if matrix.matrix.name != "rank 0":
            matrixWrapper.appendMatrix(matrix.matrix)
    print("Vertexes ", len(matrixWrapper.getVertex()))
    print("About to scatter sub vertex")
    ### new scatter
    if gatheredMatrix[0].scatterType == BUILD_ADJACENCY_LIST:
        originalArray = matrixWrapper.getVertex()
        subarraySize = len(originalArray) // 40
        subVertex = [originalArray[i * subarraySize: (i + 1) * subarraySize] for i in range(40)]
        matrix = [ProcessorWrapper(Matrix("rank " + str(i + 1)), COMPUTE_SHORTEST_DISTANCE)]
        for i, subV in enumerate(subVertex):
            matrix.append(ProcessorWrapper(Matrix("rank " + str(i + 1)), COMPUTE_SHORTEST_DISTANCE, matrixWrapper, subV))
        matrix = comm.scatter(matrix, root=0)