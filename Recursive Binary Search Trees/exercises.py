from random import sample

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
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if current_node.value > value:
            current_node.left = \
                self.__delete_node(current_node.left, value)
        elif current_node.value < value:
            current_node.right = \
                self.__delete_node(current_node.right, value)
        else:
            #left and right are empty
            if current_node.left is None and current_node.right is None:
                return None
            #left not empty, right is
            elif current_node.right is None:
                current_node = current_node.left
            #left empty, right isn't
            elif current_node.left is None:
                current_node = current_node.right
            #left and right node are not empty
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = \
                    self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    #endregion


my_tree = BinarySearchTree()


def print_it():
    print\
        ('             ', value(my_tree.root))
    print\
        ('    ', value(my_tree.root.left), '                  ', value(my_tree.root.right))
    print\
        (value(my_tree.root.left.left), '        ', value(my_tree.root.left.right))
    print\
        ('      ', value(my_tree.root.left.right.left), '     ', value(my_tree.root.left.right.right))
    print\
        ('   ', value(my_tree.root.left.right.left.left), '  ', value(my_tree.root.left.right.left.right))
    
for n in [42, 92, 91, 20, 17, 99, 84, 87, 61, 59, 31, 37, 73, 76, 64, 30, 29]:
    my_tree.r_insert(n)

print_it()

my_tree.delete_node(20)
print('\n')

print_it()

print('\n')

print(my_tree.min_value(my_tree.root))


