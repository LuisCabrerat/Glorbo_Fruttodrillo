'''
Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
LIFO last in first out
'''

stack = [1,2,3,4,5]

def push(elemento,stack):
   return stack.append(elemento)

def pop(stack):
   return stack.pop(-1)

def peek(stack):
   return stack[-1]

def isEmpty(stack):
   return not bool(stack)

def size(stack):
   return len(stack)

print(isEmpty(stack))
print(stack)

