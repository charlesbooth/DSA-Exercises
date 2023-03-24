class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ':', val)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


items = [('wholesome', 'keanu reeves'),
         ('wholesome', 'big chungus'),
         ('unwholesome', 'brody from yo mama'),
         ('unwholesome', 'ren from ren and stimpy')]

def make_table(items):
    new_table = HashTable()
    for item in items:
        new_table.set_item(*item)
    return new_table

my_hash_table = make_table(items)

my_hash_table.print_table()

print(my_hash_table.get_item('wholesome'))
print(my_hash_table.get_item('unwholesome'))
print(my_hash_table.get_item('yo mama'))

print(my_hash_table.keys())


