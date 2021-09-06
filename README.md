# simulation
Algoritmo Estable para la Exclusión Mutua en un Sistema Distribuido.
 
Esta simulación está hecha utilizando paradigma de programación orientado a objetos,
hilos de procesos y colas de procesos síncronas para simular un anillo de procesos.
 
La clase Process modela la estructura de un proceso compuesto por tres subprocesos (hilos),
del algoritmo Edsger W. Dijkstra de 1974.
 
Cada proceso consta de dos colas. Una cola lo comunica con el proceso siguiente y la otra con el proceso anterior al mismo. Las colas son el canal de comunicación entre procesos dentro de esta simulación.
 
La simulación puede ejecutar un mínimo de 2 procesos a un máximo de 10 procesos.
Para simular el acceso al recurso crítico, el proceso tres se pausa una máximo de 3 segundos.
 
Para ejecutarlo hay que escribir por la entrada estándar el número de procesos a ejecutar. Ejemplo:
 
 
$:> python3 simulation.py 5
 
 
En el ejemplo anterior la simulación ejecuta 5 procesos que desean acceder al mismo recurso crítico.
 
La probabilidad de que cada proceso requiere acceder al recurso crítico viene dada por la la relación 1/K
Donde K es la constante mayor o igual que N y N es igual al número de procesos.
 
Para detener la simulación ejecutar el comando Ctrl c