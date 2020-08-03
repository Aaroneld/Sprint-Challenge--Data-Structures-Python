import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        
        if self.value > value:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else: 
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
                
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target:
            return True
        elif self.value > target:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
             if self.right == None:
                return False
             else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.value == None:
            return None
        elif self.right == None:
            return self.value
        else:

            currentNode = self.right
            currentMax = self.right.value

            while currentNode.right != None:

                if currentNode.value < currentNode.right.value:
                    currentMax = currentNode.right.value
            
                currentNode = currentNode.right

            return currentMax 

            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        if self.value == None:
            pass
        else:
            fn(self.value)

            if self.left != None:
                self.left.for_each(fn)
            
            if self.right != None:
                self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        
        
        if self.left:
            self.left.in_order_print()
        
        print(self.value)
        
        if self.right:
            self.right.in_order_print()
                
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):

        queue = []
        currentNode = None

        if not self.value:
            pass

        queue.append(self)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        print(queue.pop(0))

        while len(queue) > 0:

            currentNode = queue[0]

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)           

            print(queue.pop(0))
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        
        queue = []
        currentNode = None

        if not self.value:
            pass

        queue.append(self)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        print(queue.pop(0))

        currentNode = queue[0]

        while currentNode != None:

            if currentNode.right:
                queue.insert(1, currentNode.right)
            
            if currentNode.left:
                queue.insert(1, currentNode.left)

            if len(queue) > 0:
                print(queue.pop(0))

                if len(queue) > 0:
                    currentNode = queue[0]
                else:
                    currentNode = None


searchTree = BSTNode(names_1[0])

[searchTree.insert(x) for ind, x in enumerate(names_1) if ind > 0]

duplicates = [x for x in names_2 if searchTree.contains(x)]

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

dict = {}

def add_to_dict(name):
    dict[name] = name

[add_to_dict(x) for x in names_1]

duplicates = [x for x in names_2 if dict.get(x) != None]

print(len(duplicates))

end_time = time.time()

print (f"runtime: {end_time - start_time} seconds")