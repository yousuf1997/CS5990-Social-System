from mpi4py import MPI
from Model import Matrix, MatrixWrapper, ProcessorWrapper
from DataReader import  DataReader
from Utills import compute_shortest_path

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dataReader = DataReader()

## scatter typoe
BUILT_ADJACENCY_LIST = "BUILT_ADJACENCY_LIST"

matrix = None

if rank == 0:
    ## populate empty matrix
    matrix = []
    for i in range(40):
        matrix.append(ProcessorWrapper(Matrix("rank " + str(i)), BUILT_ADJACENCY_LIST))
    ## if this is rank 0, it will send the data
    ## otherwise will receieve the data

comm.Barrier()

matrix = comm.scatter(matrix, root=0)

## read the file and populate the individual matrix
if rank in range(0 , 21):
    dataReader.readData("Data/twitter/twitter_combined_"+ str(rank) + ".txt", "Twitter", matrix.matrix)
else:
    pass

gatheredMatrix = comm.gather(matrix, root=0)

comm.Barrier()

if rank == 0:
    gatheredMatrix = list(gatheredMatrix)
    matrixWrapper = MatrixWrapper()
    for matrix in gatheredMatrix:
        if matrix.matrix.name != "rank 0":
            matrixWrapper.appendMatrix(matrix.matrix)
    print("Vertexes ", len(matrixWrapper.getVertex()))
    print("Shortest of 14174128 to 41728946", compute_shortest_path(matrixWrapper, "14174128", "41728946"))