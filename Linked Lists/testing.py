class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
   
class LinkedList:
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
    
    def pop_item(self):
        item = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.make_empty()
        elif self.length == 2:
            self.tail = self.head
        temp = self.head
        while temp is not None:
            if temp.next == self.tail:
                self.tail = temp
        return item


    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('\n')


my_linked_list = LinkedList(4)

my_linked_list.append_item(10)
my_linked_list.append_item('yo')
my_linked_list.append_item(4.87)

my_linked_list.print_list()


                                                                                                                    