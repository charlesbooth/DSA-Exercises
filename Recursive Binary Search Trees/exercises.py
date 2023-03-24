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
    
    #region - r_contains

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        if current_node.value > value:
            return self.__r_contains(current_node.left, value)
        if current_node.value < value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    #endregion

    #region - r_insert

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        if current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    #endregion


    #region - delete_node

    def __delete_node(self, current_node, value):
        if current_node.value > value:
            current_node.left = self.__delete_node(current_node.left, value)

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    #endregion





my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(18)
my_tree.r_insert(19)

print(value(my_tree.root))
print(value(my_tree.root.left))
print(value(my_tree.root.right))
print(value(my_tree.root.left.right))

#print(my_tree.r_contains(10))