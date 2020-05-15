import time

class BtsNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        # compare new node to node value
        if value < self.value:
            # if left doesnt exist
            if self.left is None:
                # create left if no val to left
                self.left = BtsNode(value)
            else:
                # recurse left
                self.left.insert(value)
        else:
            # value is equal or greater recurse right
            if self.right is None:
                # create right is no val to right
                self.right = BtsNode(value)
            else:
                # recurse right
                self.right.insert(value)
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BinarySearchTree
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BinarySearchTree
            if not self.right:
                return False
            return self.right.contains(target)
    # Return the maximum value found in the tree
a = BtsNode("")
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your 
bst = BtsNode(names_1[0])

for name in names_1:
    a.insert(name)

for name2 in names_2:
    if a.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
