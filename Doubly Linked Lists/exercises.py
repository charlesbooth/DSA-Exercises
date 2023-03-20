class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    #region - init
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    #endregion

    #region - append/prepend
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    #endregion

    #region - pop/popfirst
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    #endregion

    #region - get/remove
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def remove(self, index):
        if self.length == 0:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    #endregion

    #region set/insert
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True   
    #endregion

    #region - print_list/print_values
    print('list:')
    def print_list(self):
        temp = self.head
        test = \
        lambda x: x.value \
                  if hasattr(x, 'value')\
                  else x
        while temp:
            print(f'- {temp.value} \
                  (prev: {test(temp.prev)}) \
                  (next: {test(temp.next)})')
            temp = temp.next
        print('\n')

    def print_values(self):
        test = \
        lambda x: x.value \
                  if hasattr(x, 'value')\
                  else x
        print('values:')
        print('- head: ', test(self.head))
        print('- tail: ', test(self.tail))
        print('- length: ', self.length)
        print('\n')
    #endregion


items = [
            'big chungus',
            'hello',
            'hi',
            47,
            3.8,
            'yo',
            'what is up bro'
        ]


#region - make_list
def make_list(items):
    self = DoublyLinkedList(items[0])
    for i in items[1:]:
        self.append(i)
    return self
#endregion


my_doubly_linked_list = make_list(items)
my_doubly_linked_list.print_list()
my_doubly_linked_list.print_values()

my_doubly_linked_list.insert(0, 'vaporeon, da pokemon')

my_doubly_linked_list.print_list()
my_doubly_linked_list.print_values()