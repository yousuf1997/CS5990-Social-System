from mpi4py import MPI
from Model import Matrix, MatrixWrapper
from DataReader import  DataReader

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dataReader = DataReader()

matrix = None

if rank == 0:
    ## populate empty matrix
    matrix = []
    for i in range(20):
        matrix.append(Matrix("rank " + str(i)))
    ## if this is rank 0, it will send the data
    ## otherwise will receieve the data

matrix = comm.scatter(matrix, root=0)

if rank in range(20):
    ## read the file and populate the individual matrix
    dataReader.readData("Data/twitter/twitter_combined_"+ str(rank + 1) + ".txt", "Twitter", matrix)
    # print(rank, matrix.getMatrix())

gatheredMatrix = comm.gather(matrix, root=0)

if rank == 0:
    gatheredMatrix = list(gatheredMatrix)
    matrixWrapper = MatrixWrapper()
    for matrix in gatheredMatrix:
        matrixWrapper.appendMatrix(matrix)
