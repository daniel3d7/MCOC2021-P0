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




# DESEMPEÑO MATMUL



¿Cómo difiere del gráfico del profesor/ayudante?

Viendo el gráfico "tamaño de matriz vs tiempo transcurrido", se nota cómo mi computador se demoró más que el del profesor en realizar las corridas, especialmente los últimos puntos correspondientes a matrices cuadradas de dimensión 10000, donde se alcanzaron tiempos alrededores de 1 minuto, mientras que el profesor se demoró 30 segundos máximo aproximadamente. Por otro lado, el gráfico de uso de memoria es idéntico al del profesor, ya que, independientemente del computador que se tiene, las matrices que se arman ocupan el mismo espacio.

¿A qué se pueden deber las diferencias en cada corrida?

Estas diferencias se deben a múltiples factores. Uno de estos es el hecho de que, en mi computador, se tienen se tienen diferentes procesos que se están realizando a la vez, los cuales influyen en el tiempo en que se ejecuta el código. Otro factor puede ser el hecho de que python, al usar la memoria, tiene el siguiente orden: caché, RAM, disco. Cada vez que necesita usar más memoria, tiene que ir de una fuente a otra, y estos cambios de memoria son variables, generando diferencias entre los tiempos de ejecución de cada corrida del código.

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
A medida que va aumentando el tamaño de la matriz, también sube el uso de memoria. Este incremento es lineal debido a que cada dimensión extra que se le agrega a la matriz ocupa el mismo espacio. Por otro lado, a diferencia del uso de memoria, el tiempo transcurrido no tiene un comportamiento lineal, debido a que, al aumentar el tamaño de la matriz, también se incrementa la cantidad de operaciones a realizar pero de manera exponencial, lo cual genera que el PC necesite un tiempo exponencialmente mayor para efectuar las operaciones. Un ejemplo que explica este fenómeno es el siguiente: se quiere multiplicar dos matrices de 2x2 y otras dos de 4x4. Las matrices 2x2 ocupan un espacio equivalente a un cuarto (aproximadamente) al que ocupan las matrices 4x4, y esto es solo debido a su tamaño, es decir, el uso de memoria es lineal con el tamaño de la matriz. Sin embargo, la cantidad de operaciones a realizar al multiplicar las matrices 2x2 es 12, mientras que las de 4x4 es 112. Este incremento es exponencial lo cual provoca que el tiempo necesario para realizar dichas operaciones también aumente exponencialmente.

¿Qué versión de python está usando?

Estoy usando Python 3.8.5

¿Qué versión de numpy está usando?
Estoy usando Numpy 1.19.2

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.
A continuación, se presenta una imagen que muestra el uso del procesador, donde se ven los 4 núcleos y su actividad.


