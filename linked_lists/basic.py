'''
Linked List operations:
Traversal
remove node
insert node
sort
'''
class Node:
   def __init__(self,data:int):
      self.next = None
      self.data = data

def remove_node(root: Node, value: int) -> Node:
    if root !=None and root.data == value:
        new_root = root.next
        del root                
        return new_root

    current = root
    while current.next !=None and current.next.data != value:
        current = current.next

    if current.next == None:
        return root

    node_to_remove = current.next
    current.next = node_to_remove.next
    del node_to_remove              

    return root

def traverse(root):
   current_position=root
   
   while current_position !=None:
      print(current_position.data,end="->")
      current_position=current_position.next
   print("None")
   return

def insertNodeAtPosition(root, newNode, position):
  if position == 1:
    newNode.next = root
    return newNode

  current = root
  for _ in range(position - 2):
    if current is None:
      break
    current = current.next

  newNode.next = current.next
  current.next = newNode
  return root

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

#node1=remove_node(node1,1)
#traverse(node1)
new=Node(99)
traverse(node1)
node1=insertNodeAtPosition(node1,new,2)
traverse(node1)




