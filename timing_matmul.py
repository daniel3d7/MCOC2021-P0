from scipy import matmul, rand
from time import perf_counter
from numpy import zeros , float16,float32,float64
import matplotlib.pylab as plt

N = 1000
Ns = [1, 2, 3, 5, 7, 10, 15, 21, 30, 42, 60, 84, 119, 167, 236, 332, 467, 657, 925, 1301, 1831, 2577, 3626, 5102, 7179]


dts = []

mems = []

fid = open("rendimiento.txt", "w")

contador = 0

while contador < 10 :
    
    for N in Ns:
    

        A = zeros((N,N), dtype = float32() ) + 1
        uso_memoria_teorico = 4*N*N
        uso_memoria_numpy = A.nbytes
    
 
    
   
        B = zeros((N,N)) + 2


        t1 = perf_counter()

        C = A@B

        t2 = perf_counter()
    
        uso_memoria_total = A.nbytes + B.nbytes + C.nbytes
        dt = t2 - t1
        dts.append(dt)
    
        mems.append(uso_memoria_total)
    
        print (f"N = {N}  dt = {dt} s")
    
        fid.write(f"{N}  {dt}  {uso_memoria_total} \n")
    contador += 1

fid.close()


