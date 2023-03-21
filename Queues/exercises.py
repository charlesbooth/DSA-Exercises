class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    #region - print_stack
    def print_stack(self, label='list'):
        print(label + ': ')
        temp = self.first
        while temp is not None:
            print(temp.value if hasattr(temp, 'value') else temp)
            temp = temp.next
        print('\n')
    #endregion

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.front = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue('big chungus')
my_queue.enqueue('yo mama')
my_queue.enqueue(47)
my_queue.print_stack('queue')
print('first:', my_queue.first.value)
print('last:', my_queue.last.value)
print('length:', my_queue.length, '\n')

dequeued = my_queue.dequeue()
print('dequeued:', dequeued.value, '\n')

my_queue.print_stack()
print('first:', my_queue.first.value \
      if hasattr(my_queue.first, 'value') else my_queue.first)
print('last:', my_queue.last.value \
      if hasattr(my_queue.last, 'value') else my_queue.first)
print('length:', my_queue.length)