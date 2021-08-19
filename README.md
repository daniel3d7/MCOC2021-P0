# MCOC2021-P0

# Mi computador principal

* Marca/modelo: DESKTOP-2RBRNRH
* Tipo: PC
* Año adquisición: 2012
* Procesador:
  * Marca/Modelo: Intel(R) Core(TM) i5-3330 CPU @ 3.00GHz
  * Velocidad Base: 3.00 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 2
  * Arquitectura: x86_64
* Tipo de Sistema
  * Sistema operativo de 64 bits, procesador basado en x64
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 1666 MHz
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce GTX 650
  * Memoria dedicada: 8192 MB
  * Resolución: 1920 x 1080


* Dirección IP (Interna, del router): 192.168.0.179
* Dirección IP (Externa, del ISP): 190.45.122.34
* Proveedor internet: Movistar Banda Ancha S.A.




# DESEMPEÑO MATMUL (Entrega 2)



¿Cómo difiere del gráfico del profesor/ayudante?

Analizando el gráfico , se pudo ver que no se logro obtener los graficos adecuado, esto se debe a que hubieron ciertos problemas con el codigo en la construccion de los graficos, pero se puede notar que si existe un aumento en el uso de la memoria alcanzando casi el maximo de memoria que soporta mi computador ( 8Gb Ram), claramente se demoró un mayor tiempo de procesamiento al aumentar el N , especialmente los últimos puntos correspondientes a matrices cuadradas de dimensión 8000, donde se alcanzaron tiempos alrededores de mas de 10 segundos, mientras que el profesor se demoró 7 segundos máximo aproximadamente. 

¿A qué se pueden deber las diferencias en cada corrida?

Esto puede ocurrir debido a distintos factores como que el computador trabaja realizando varias actividades al mismo tiempo, por lo cual entre cada una de estas corridas el computador varia en las acciones que realiza lo cual demuestra los cambios en los tiempos y usos de memoria.  

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

Podemos ver que a medida que se aumenta el tamaño de la matriz, también sube el uso de memoria. Este incremento es lineal debido a que al aumentar las dimensiones aumenta linealmente el uso de memoria en cada uno de estas, por lo que no existe variacion en este sentido como lo es en el caso del tiempo de procesamiento, donde el tiempo transcurrido no tiene un comportamiento lineal, debido a que, al aumentar el tamaño de la matriz, también se incrementa la cantidad de operaciones a realizar pero de manera exponencial, lo cual genera que el PC necesite un tiempo exponencialmente mayor para efectuar las operaciones. 

¿Qué versión de python está usando?

Estoy usando Python 3.8.5

¿Qué versión de numpy está usando?
Estoy usando Numpy 1.19.2

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.
A continuación, se presenta una imagen que muestra el uso del procesador, donde se ven los 4 núcleos y su actividad.

SE ADJUNTA FOTOS DE CPU NUCLEOS EN REPOSITORIO.



# Desempeño de Inv (Entrega 3)

Analizando los resultados obtenidos pudimos notar que los tipos de datos half y longdouble no son admisibles para numpy.linalg.inv, debido a que el sistema no los soporta por la codificacion de la libreria. 

Por otro lado al realizar un analizis de los graficos obtenidos, se puede ver como disminuyen notablemente los tiempos de ejecucion al usar overwrite_a = True.

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 
Podemos ver que se utiliza :
Libreria Numpy : Ejecutado con numpy.linalg.solve(MatrixNxN, I), donde se utiliza la factorizacion LU (Lapack) mediante solve.
Libreria Scipy : Ejecutado con scypy.linalg.inv(), tambien utiliza Lapack pero es optimizado por Atlas y Blas. Dado esto los tiempos de ejecucion son menores ya que los procesos se realizan rapidamente utilizando funciones del algebra lineal.

¿Cómo incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.

Analizando los graficos obtenidos , se ve que el half toma menos tiempo en invertir la matriz, dado que tiene datos más pequeños que los single, double y longdouble. Estos cambios en el tiempo entre estos tipos es debido al paralelismo, en donde el procesador ejecuta varias tareas al mismo tiempo, realizando varios cálculos simultáneamente. Esto se verifica al revisar el uso de memoria en la ejecucion de cada uno de los codigos, teniendo en cuenta que el pc mientras realiza las operaciones, al mismo tiempo de manera paralela ejecuta ciertos procesos externos a python gracias a la memoria cache y al paralelismo 





