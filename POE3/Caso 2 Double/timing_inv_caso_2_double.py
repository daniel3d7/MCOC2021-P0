from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt
import random
from numpy.linalg import inv
import numpy as np
from scipy import linalg


# LAPLACIANA

def laplaciana_double(N, dtype=np.double):
	A = zeros((N, N), dtype=dtype)

	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i-j) == 1:
				A[i,j] = -1
				A[j,i] = -1

	return A


# CONSTRUCCION DE .txt DE MEMORIA Y TIEMPO UTILIZADO PARA CADA MATRIZ

titulo_archivo = "Caso 2 Double"

a = float64



# Se utilizan Ns no muy altos debido a que la capacidad de memoria ram en mi pc no es muy elevada.

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

tiempo = []
memoria =[]

for i in range(10):
	fid = open(f"Rendimiento {titulo_archivo}{i}.txt", "w")

	for N in Ns:
		
		
		A = laplaciana_double(N, dtype=a)
		t1 = perf_counter()
		
		Am1 = linalg.inv(A, overwrite_a=False)

		t2 = perf_counter()
		
		dt = t2 - t1
		
		bytes_total = A.nbytes + Am1.nbytes

		tiempo.append(dt)
		memoria.append(bytes_total)

		print(f"N = {N} dt = {dt} s memoria = {bytes_total} bytes flops = {N**3/dt} flops/s")
		
		fid.write(f"{N} {dt} {bytes_total}\n")

	fid.close()



# GRAFICOS
# SE PROCEDE A GRAFICAR DE ACUERDO A LOS TXT


Ns = []
dts = []
mems = []



for i in range(10):	
	fid = open(f"Rendimiento {titulo_archivo}{i}.txt", "r")	

	for line in fid:
		sl = line.split()
		N = int(sl[0])
		dt = float(sl[1])
		mem = int(sl[2])

		Ns.append(N)
		dts.append(dt)
		mems.append(mem)

	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000", "20000"]

ejedy_Uso = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11]
ejey_Uso = ["1 KB","10 KB", "100 KB", "1 MB","10 MB", "100 MB", "1 GB", "10 GB", ""]


plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Desempeño Inv {titulo_archivo}")

M = 10
for i in range(M):
	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso, [])
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

#gráfico uso de memoria

plt.subplot(2, 1, 2)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (s)")
plt.loglog(Ns, mems, marker="o")
plt.xticks(ejedx_Uso, ejex_Uso, rotation=45)
plt.yticks(ejedy_Uso, ejey_Uso)
plt.axhline(y=8*10**9 , linestyle="--", color="k")

plt.grid(b=True)



plt.show()