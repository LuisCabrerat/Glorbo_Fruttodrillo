'''
STACKS (LIFO)

Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
LIFO last in first out
'''

my_stack : list[int] = [1,2,3,4,5]

def push(elemento:int,stack:list[int])->None:
   stack.append(elemento)
   return None

def pop(stack:list[int])->int:
   return stack.pop(-1)

def peek(stack:list[int])->int:
   return stack[-1]

def isEmpty(stack:list[int])->bool:
   return not bool(stack)

def size(stack:list[int])->int:
   return len(stack)