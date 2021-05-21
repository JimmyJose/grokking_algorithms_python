def sort(list):
    if len(list) < 2:
        return list
    
    pivot_index = len(list) // 2
    pivot = list.pop(pivot_index)
    less = [i for i in list if i<= pivot]
    greater = [i for i in list if i > pivot]

    return sort(less) + [pivot] + sort(greater)
