class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def return_values(self):

        currentNode = self.head

        while currentNode != None:
            print(currentNode.value)
            currentNode = currentNode.next_node

    def reverse_list(self, node, prev = None):
          
       curr = node
       nex = None 

       if curr:
        nex = curr.next_node
        
       while curr:
           
           curr.set_next(prev)  

           prev = curr
           curr = nex
           if nex:
               nex = nex.next_node

    
       self.head = prev


list = LinkedList()

list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)

# list.return_values()

list.reverse_list(list.head)
list.return_values()




