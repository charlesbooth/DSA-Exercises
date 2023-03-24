class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self, label='graph'):
        print('\n')
        print(label + ':')
        for k, v in self.adj_list.items():
            print('- ', k, ':', v)
        print('\n')

    def add_vertex(self, value):
        if value not in self.adj_list:
            self.adj_list.setdefault(value, {})
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 == v2:
            return False
        if not all(v in self.adj_list for v in (v1, v2)):
            return False
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].setdefault(v2)
            self.adj_list[v2].setdefault(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        check = lambda v1, v2: v1 in self.adj_list[v2]
        if all((check(v1, v2), check(v2, v1))):
            del self.adj_list[v1][v2]
            del self.adj_list[v2][v1]
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for k in self.adj_list[vertex].keys():
                del self.adj_list[k][vertex]
            del self.adj_list[vertex]
            return True
        return False

     
my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)

print(my_graph.add_edge(1, 2))
print(my_graph.add_edge(2, 3))
print(my_graph.add_edge(3, 4))
print(my_graph.add_edge(4, 5))
print(my_graph.add_edge(2, 5))

my_graph.print_graph('before remove')

print(my_graph.remove_vertex(2), '<--- removed')

my_graph.print_graph('after remove')

