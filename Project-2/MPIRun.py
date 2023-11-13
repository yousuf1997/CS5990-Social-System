from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None

if rank == 0:
    data = [[], [], []]

data = comm.scatter(data, root=0)

if rank in [1,2]:
    data.append("rank " + str(rank))
    print(rank, data)

gathered_data = comm.gather(data, root=0)

if rank == 0:
    print(rank, gathered_data)