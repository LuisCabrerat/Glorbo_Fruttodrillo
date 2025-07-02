'''
QUEUE  (FIFO)

ENQUEUE
DEQUEUE
PEEK
isEmpty
Size
'''

my_queue : list[int] = [1,2,3,4]

def enqueue(cola:list[int],elemento:int)->None:
   cola.append(elemento)
   return None

def dequeue(cola:list[int])->int:
   return cola.pop(0)

def peek(cola:list[int])->int:
   return cola[0]

def isEmpty(cola:list[int])->bool:
   return not bool(cola)  #false si esta vacio, true si lleno

def size(cola:list[int])->int:
   return len(cola)