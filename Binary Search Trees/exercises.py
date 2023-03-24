import sys
sys.path.append('.')
from functions.my_functions import value

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    #region - insert
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node == temp:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    #endregion

    #region - contains
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    #endregion

my_tree = BinarySearchTree()

my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(7)
my_tree.insert(5)
my_tree.insert(6)
my_tree.insert(1)
my_tree.insert(4)

print(value(my_tree.root))
print(value(my_tree.root.left))
print(value(my_tree.root.right))

my_tree.contains(4)