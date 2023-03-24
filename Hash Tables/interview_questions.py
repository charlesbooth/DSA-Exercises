list1 = [1, 3, 5]
list2 = [2, 4, 5]

def same_items1(list1, list2):
    d = {}
    for i in list1:
        d.setdefault(i, True)
    for j in list2:
        if j in d:
            return True
        
def same_items2(list1, list2):
    return bool(set(list1) and set(list2))

        
result1 = same_items1(list1, list2)
print(result1)

result2 = same_items2(list1, list2)
print(result2)