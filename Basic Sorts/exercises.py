def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([4,5,4,8,1,7,1,15,4,1,8,2,1,8,7,5,1,8]))

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in my_list[i:]:
            if j < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

print(selection_sort([1, 2, 6, 5, 4, 3]))

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

print(insertion_sort([1,5,4,3,6,1,4,6,78,7,4]))