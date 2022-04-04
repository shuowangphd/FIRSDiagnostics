import hazel
import os

iterator = hazel.Iterator(use_mpi=True)
mod = hazel.Model('conf3.ini', rank=iterator.get_rank(),
                  working_mode='inversion')
iterator.use_model(model=mod)
iterator.run_all_pixels()

"""
cd 
mpiexec -n 3 python inve.py
 
"""
