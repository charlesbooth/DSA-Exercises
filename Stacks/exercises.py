class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self, label='list'):
        print(label + ': ')
        temp = self.top
        while temp is not None:
            print(temp.value if hasattr(temp, 'value') else temp)
            temp = temp.next
        print('\n')

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

items = [
            'big chungus',
            'among us',
            'wholesome',
            42
        ]

def make_stack(items, label='list'):
    stack = Stack(items[0])
    for i in items[1:]:
        stack.push(i)
    return stack


my_stack = make_stack(items)
my_stack.print_stack()

popped = my_stack.pop()

my_stack.print_stack()

print('popped:', popped.value)
