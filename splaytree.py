import random
import time


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class EmptyTreeException(Exception):
    pass

class DuplicateKeyException(Exception):
    pass

class TreeTraversal:
    def traverse(self, root, result):
        raise NotImplementedError

class InOrderTraversal(TreeTraversal):
    def traverse(self, root, result):
        if root:
            self.traverse(root.left, result)
            result.append(root.key)
            self.traverse(root.right, result)

class PreOrderTraversal(TreeTraversal):
    def traverse(self, root, result):
        if root:
            result.append(root.key)
            self.traverse(root.left, result)
            self.traverse(root.right, result)

class PostOrderTraversal(TreeTraversal):
    def traverse(self, root, result):
        if root:
            self.traverse(root.left, result)
            self.traverse(root.right, result)
            result.append(root.key)

class SplayTree:
    PRE_ORDER = PreOrderTraversal()
    IN_ORDER = InOrderTraversal()
    POST_ORDER = PostOrderTraversal()

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)
        self.root = self._splay(self.root, key)
    
    # define a funtion to find the number of nodes between root and the key
    def number_of_nodes(self, key):
        def count_nodes(node, key):
            if node is None:
                return 0
            if node.key == key:
                return 1
            elif key < node.key:
                return 1 + count_nodes(node.left, key)
            else:
                return 1 + count_nodes(node.right, key)
        
        if self.root is None:
            return 0
        return count_nodes(self.root, key)

    

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def delete(self, key):
        if self.is_empty():
            raise EmptyTreeException("Cannot delete from an empty tree")

        self.root = self._splay(self.root, key)

        if self.root.key != key:
            return

        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root
            self.root = self._splay(self.root.left, self._find_max(self.root.left).key)
            self.root.right = temp.right

    def traverse(self, traversal):
        result = []
        traversal.traverse(self.root, result)
        return result

    def _find_max(self, root):
        while root.right:
            root = root.right
        return root

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key > key:
            if root.left is None:
                return root
            if root.left.key > key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif root.left.key < key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._rotate_left(root.left)
            return root if root.left is None else self._rotate_right(root)
        else:
            if root.right is None:
                return root
            if root.right.key > key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._rotate_right(root.right)
            elif root.right.key < key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            return root if root.right is None else self._rotate_left(root)

    def _insert_rec(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        else:
            raise DuplicateKeyException(f"Duplicate key: {key}")
        return root
    



# # write a code for testing the splay tree
# def test_splay_tree():
#     tree = SplayTree()
#     assert tree.is_empty() == True
#     tree.insert(100)
#     tree.insert(50)
#     tree.insert(200)
#     tree.insert(25)
#     tree.insert(75)
#     tree.insert(150)
#     # tree.insert(250)
#     tree.insert(30)
#     tree.insert(60)
#     tree.insert(90)
#     tree.insert(125)
#     tree.insert(175)
#     tree.insert(225)
#     tree.insert(275)
#     assert tree.search(30) == True
#     assert tree.search(60) == True
#     assert tree.search(90) == True
#     assert tree.search(125) == True
#     assert tree.search(175) == True
#     assert tree.search(225) == True
#     assert tree.search(275) == True
#     assert tree.search(100) == True
#     assert tree.search(50) == True
#     assert tree.search(200) == True
#     assert tree.search(25) == True
#     assert tree.search(75) == True
#     assert tree.search(150) == True
#     assert tree.search(250) == False
#     assert tree.is_empty() == False
#     # assert tree.traverse(SplayTree.PRE_ORDER) == [30, 25, 50, 60, 90, 75, 100, 250, 225, 200, 175, 150, 125, 275]
#     # assert tree.traverse(SplayTree.IN_ORDER) == [25, 30, 50, 60, 75, 90, 100, 125, 150, 175, 200, 225, 250, 275]
#     # assert tree.traverse(SplayTree.POST_ORDER) == [25, 30, 75, 90, 60, 50, 125, 150, 175, 200, 225, 275, 250, 100]
#     tree.delete(30)
#     tree.delete(60)
#     tree.delete(90)
#     tree.delete(125)
#     tree.delete(175)
#     tree.delete(225)
#     tree.delete(275)
#     tree.delete(100)
#     tree.delete(50)
#     tree.delete(200)
#     tree.delete(25)
#     tree.delete(75)
#     tree.delete(150)
#     # tree.delete(250)

#     assert tree.is_empty() == True
#     print("All tests passed")

# test_splay_tree()
# generate a random number between 0 and 1


# generate distinct random numbers
def generate_random_numbers(n):
    return random.sample(range(1, 10*n), n)

# find the first number that is not in the list of random numbers generated
def find_missing_number(list_of_numbers,n):
    for i in range(1, 10*n):
        if i not in list_of_numbers:
            return i
list_to_plot = []
C = random.random()
for i in range(20,50):
    n = 100*i
    a = random.randint(100,110)
    m = a*n
    tup = (n,m,C)
    print(tup)
    random_numbers = generate_random_numbers(n)
    # insert the random numbers into the splay tree
    tree = SplayTree()
    for number in random_numbers:
        tree.insert(number)
    first_missing_number = find_missing_number(random_numbers,n)
    # i want to generate a andom sequence  of numbers from the list of random numbers of size (1-C)*m with repetition
    random_sequence = random.choices(random_numbers, k=int((1-C)*m))
    # in between the random sequence at random positions i want to insert the first missing number for C*m times
    '''made an edit'''
    tree.search(first_missing_number)
    c_m = int(C*m)
    for i in range(c_m):
        random_sequence.insert(random.randint(0,len(random_sequence)),first_missing_number)
    # search for the each number in the random sequence in the splay tree
    steps_taken = 0
    
    for number in random_sequence:
        if number == first_missing_number:
            steps_taken += tree.number_of_nodes(number)
            tree.search(number)
        else:
            tree.search(number)
    list_to_plot.append((n,steps_taken/c_m))
        
print(list_to_plot)

import matplotlib.pyplot as plt

x = [i[0] for i in list_to_plot]
y = [i[1] for i in list_to_plot]
plt.plot(x,y)
plt.xlabel("n")
plt.ylabel("Steps taken")
plt.title("Time taken to search for the first missing number in a splay tree")
# plt.yticks([2.5,3.5,4.5])  # Set range to zoom in on data

plt.show()

with open("testcase.txt","w") as f:
    for i in list_to_plot:
        f.write(f"{i[0]},{i[1]}\n")



    
    