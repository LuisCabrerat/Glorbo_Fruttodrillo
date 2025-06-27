'''
QUEUE  (FIFO)

ENQUEUE
DEQUEUE
PEEK
isEmpty
Size
'''

queues = [1,2,3,4]

def enqueue(cola,elemento):
   return cola.append(elemento)

def dequeue(cola):
   return cola.pop(0)

def peek(cola,elemento):
   return cola[0]

def isEmpty(cola):
   return not bool(cola)  #false si esta vacio, true si lleno

def size(cola):
   return len(cola)

