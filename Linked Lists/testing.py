class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
   
class LinkedList:
    #region - top
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append_item(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend_item(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = self.head
        self.length += 1
        return True
    
    def index_item(self, index):
        if not 0 <= index < self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_item(self, index, value):
        temp = self.index_item(index)
        if not temp:
            print('Index does not exist.', '\n')
            return False
        temp.value = value
        return True
    
    def insert_item(self, index, value):
        if not 0 <= index <= self.length:
            return False
        if index == 0:
            return self.prepend_item(value)
        if index == self.length:
            return self.append_item(value)
        temp = self.index_item(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node   
        self.length += 1
        return True
    
    def remove_item(self, index):
        if not 0 <= index <= self.length:
            return None
        if index == 0:
            return self.pop_left()
        if index == self.length - 1:
            return self.pop_right()
        prev = self.index_item(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    #endregion
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


            




    #region - bottom
    def pop_right(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.make_empty()
        return temp
 
    def pop_left(self):
        if self.length == 0:
            return None
        temp = self.head
        self.length -= 1
        if self.length == 0:
            self.make_empty()
        else:
            self.head = self.head.next
        temp.next = None
        return temp
        
    def make_empty(self):
        self.head = None
        self.tail = None
        if self.length != 0:
            self.length = 0

    def print_list(self):
        temp = self.head
        print('list:')
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('\n')
#endregion


items = [
            'big chungus',
            'among us'
        ]

def make_list(list_items):
    new_list = LinkedList(list_items[0])
    for i in list_items[1:]:
        new_list.prepend_item(i)
    return new_list

#make list
my_linked_list = make_list(items)

def print_values(list_object=my_linked_list):
    print('head: ', list_object.head.value)
    print('tail: ', list_object.tail.value)
    print('length: ', list_object.length)
    print('\n')

#etc.

my_linked_list.print_list()
print_values()

#region - test inserts, pops, etc.
# #print(my_linked_list.insert_item(3, 'hello there!'), '<-----')
# item = my_linked_list.remove_item(2)
# print(item.value, '<-----')
# #my_linked_list.pop_left()
# print('\n')
#endregion
my_linked_list.reverse()

my_linked_list.print_list()
print_values()




















#region - unused code
#my_linked_list.prepend_item('big mama')

# my_linked_list.print_list()

# popped = my_linked_list.pop_left()

# my_linked_list.print_list()

# print('value:', popped)
# print('\n')

# my_linked_list.print_list()



# #my_linked_list.append_item('yo')

# # print('before:')
# # my_linked_list.print_list()

# # print(my_linked_list.pop_right())
# # print(my_linked_list.pop_right())
# # print(my_linked_list.pop_right())

# #print(f'value: {popped.value}', '\n')

# # print('after:')
# # my_linked_list.print_list()
# print('head: ', my_linked_list.head)
# print('tail: ', my_linked_list.tail)
# print('length: ', my_linked_list.length)
#endregion

                                                                                                                    