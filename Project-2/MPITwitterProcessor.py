from mpi4py import MPI
from Model import Matrix, MatrixWrapper
from DataReader import  DataReader
from Utills import compute_shortest_path

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dataReader = DataReader()

matrix = None

if rank == 0:
    ## populate empty matrix
    matrix = []
    for i in range(21):
        matrix.append(Matrix("rank " + str(i)))
    ## if this is rank 0, it will send the data
    ## otherwise will receieve the data

comm.Barrier()

matrix = comm.scatter(matrix, root=0)

## read the file and populate the individual matrix
dataReader.readData("Data/twitter/twitter_combined_"+ str(rank) + ".txt", "Twitter", matrix)
        # print(rank, matrix.getMatrix())

gatheredMatrix = comm.gather(matrix, root=0)

comm.Barrier()

if rank == 0:
    gatheredMatrix = list(gatheredMatrix)
    matrixWrapper = MatrixWrapper()
    for matrix in gatheredMatrix:
        if (matrix.name != "rank 0"):
            matrixWrapper.appendMatrix(matrix)
    print("Vertexes ", len(matrixWrapper.getVertex()))
    print("Shortest of 100581193 to 47401917" , compute_shortest_path(matrixWrapper, "100581193", "47401917"))
