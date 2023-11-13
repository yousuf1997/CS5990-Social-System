from mpi4py import MPI
from Model import Matrix, MatrixWrapper
from DataReader import  DataReader

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
dataReader = DataReader()

matrixList = None

if rank == 0:
    ## populate empty matrix
    matrixList = []
    for i in range(20):
        matrixList.append(Matrix())

## if this is rank 0, it will send the data
## otherwise will receieve the data
matrix = comm.scatter(matrixList, root=0)

gatheredMatrix = comm.gather(matrixList, root=0)

if rank in range(20):
    ## read the file and populate the individual matrix
   dataReader.readData("Data/twitter/twitter_combined_"+ str(rank + 1) + ".txt", "Twitter", matrix)

if rank == 0:
    ## use the gathered matrix to populate the wrapper
    matrixWrapper = MatrixWrapper()
    for matrix in gatheredMatrix:
        matrixWrapper.appendMatrix(matrix)
