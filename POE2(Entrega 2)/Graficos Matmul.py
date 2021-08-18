

from scipy import matmul, rand
from time import perf_counter
from numpy import zeros , float16,float32,float64
import matplotlib.pylab as plt

tiempo = []
largo = [] 
memoria = []


file = open("rendimiento.txt", "r")


lineas=file.readlines()
for linea in lineas:
    linea1 = list(linea.split())
    
   
  
    
    if len (linea1) == 3:
        tiempo.append(float(linea1[1])); memoria.append(float(linea1[2])); largo.append(float(linea1[0]))


    
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
y_time = [1e-4, 0.001, 0.01, 0.1, 1, 10, 60, 600] #ticks
y_labels = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
y_memory = [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]
y_mlabels = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.ylabel("Tiempo transcurrido (s)")


for Z in tiempo:
    plt.loglog(largo[0],Z)
    plt.plot(largo[0],Z,marker='o')
plt.yticks(y_time, y_labels)
plt.xticks(x,[],rotation = 70)
plt.grid()



plt.subplot(2,1,2)
plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (s)")
plt.axhline(y=16000, color='black', linestyle='--')


for pasos in memoria:
    plt.loglog(largo[0],pasos)
    plt.scatter(largo[0],pasos)
    plt.plot(largo[0],pasos)

plt.yticks(y_memory,y_mlabels)
plt.xticks(x,x,rotation = 70)
plt.grid()



plt.show()
file.close()
