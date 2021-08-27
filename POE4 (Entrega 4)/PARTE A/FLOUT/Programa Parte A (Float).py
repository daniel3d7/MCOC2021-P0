
from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt
import random
from numpy.linalg import inv
import numpy as np
from scipy import linalg


# LAPLACIANA

def laplaciana_double(N, dtype=np.single):
	A = zeros((N, N), dtype=dtype)

	for i in range(N):
		A[i,i] = 2
		for j in range(max(0,i-2),i):
			if abs(i-j) == 1:
				A[i,j] = -1
				A[j,i] = -1

	return A

def vector(N):
    vector = []
    for i in range(N):
        vector.append(1)
    
    b = np.array(vector)
    return b
        
    
  




    
# Se utilizan Ns no muy altos debido a que la capacidad de memoria ram en mi pc no es muy elevada.

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []



#########################  I)  AX = B #################################################

titulo_archivo = "Caso I (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        Am1 = inv(A)
        x = Am1*vector(N)
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
 	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

 	for line in fid:
         
		 sl = line.split()
		 N = int(sl[0])
		 dt = float(sl[1])
		

		 Ns.append(N)
		 dts.append(dt)
		

 	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
 	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()


# #########################  II)  UTILIZANDO SCIPY  #################################################


Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []


titulo_archivo = "Caso II (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        x = linalg.solve(A,vector(N))
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
 	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

 	for line in fid:
		 sl = line.split()
		 N = int(sl[0])
		 dt = float(sl[1])
		

		 Ns.append(N)
		 dts.append(dt)
		

 	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
 	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()


#########################  III)  UTILIZANDO SCIPY CON asumme_a = "poss"  #################################################


Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []


titulo_archivo = "Caso III (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        x = linalg.solve(A,vector(N),assume_a="pos")
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
 	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

 	for line in fid:
		 sl = line.split()
		 N = int(sl[0])
		 dt = float(sl[1])
		

		 Ns.append(N)
		 dts.append(dt)
		

 	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
 	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()



#########################  IV)  UTILIZANDO SCIPY CON asumme_a = "sym"  ################################

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []


titulo_archivo = "Caso IV (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        x = linalg.solve(A,vector(N),assume_a="sym")
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
 	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

 	for line in fid:
		 sl = line.split()
		 N = int(sl[0])
		 dt = float(sl[1])
		

		 Ns.append(N)
		 dts.append(dt)
		

 	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
 	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()



#########################  V)  UTILIZANDO SCIPY CON overwrite_a = "true"  ################################

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []


titulo_archivo = "Caso V (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        x = linalg.solve(A,vector(N),overwrite_a=True)
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
 	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

 	for line in fid:
 		 sl = line.split()
 		 N = int(sl[0])
 		 dt = float(sl[1])
		

 		 Ns.append(N)
 		 dts.append(dt)
		

 	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
 	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()

########################  VI)  UTILIZANDO SCIPY CON overwrite_b = "true"  ################################

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []


titulo_archivo = "Caso VI (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        x = linalg.solve(A,vector(N),overwrite_b=True)
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
 	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

 	for line in fid:
		 sl = line.split()
		 N = int(sl[0])
		 dt = float(sl[1])
		

		 Ns.append(N)
		 dts.append(dt)
		

 	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
 	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()

########################  VII)  UTILIZANDO SCIPY CON overwrite_b = "true"  ################################

Ns = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 16, 20, 24, 29, 35, 42, 51, 
62, 75, 100, 190, 200, 240, 330, 360, 400, 490, 500, 540, 596, 719, 868, 900, 1048, 
1264, 1526, 1842, 2222, 2500,4000]

a = float32
tiempo = []


titulo_archivo = "Caso VII (float)"
fid = open(f"Rendimiento {titulo_archivo}.txt", "w")

lista_sumada = []

for i in range(10):
    
    lista = []
    for N in Ns:
        
        
        A = laplaciana_double(N, dtype=a)
        t1 = perf_counter()
        
        x = linalg.solve(A,vector(N),overwrite_a=True,overwrite_b=True)
        t2 = perf_counter()
        dt = t2 - t1
        
        
        lista.append(dt)
        	
        print(f"N = {N} dt = {dt} s ")
    lista_sumada.append(lista)
    


c = 0

for listas in lista_sumada:
    c += np.array(listas)

lista_final = []
i = 0
for numeros in c :
    lista_final.append(numeros/10)
    
    fid.write(f"{Ns[i]} {numeros/10}\n")
    i +=1

fid.close()


Ns = []
dts = []




for i in range(10):	
	fid = open(f"Rendimiento {titulo_archivo}.txt", "r")	

	for line in fid:
		sl = line.split()
		N = int(sl[0])
		dt = float(sl[1])
		

		Ns.append(N)
		dts.append(dt)
		

	fid.close()


ejed_Tiempo = [1e-4, 1e-3, 1e-2, 1e-1, 1, 10, 60, 600]
eje_Tiempo = ["0.1 ms","1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

ejedx_Uso = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
ejex_Uso = ["10","20", "50", "100","200", "500", "1000", "2000", "5000", "10000"]




plt.figure()

#gráfico tiempo transcurrido

plt.subplot(2, 1, 1) #dos filas 1 columna
plt.title(f"Tiempo de respuesta {titulo_archivo}")

M = 10

for i in range(M):
	plt.loglog(Ns[i*M:(i+1)*M], dts[i*M:(i+1)*M], marker="o")
plt.ylabel("Tiempo transcurrido (s)")
#plt.loglog(Ns, dts, marker="o")
plt.xticks(ejedx_Uso,ejex_Uso)
plt.yticks(ejed_Tiempo, eje_Tiempo)

plt.grid(b=True)

plt.show()