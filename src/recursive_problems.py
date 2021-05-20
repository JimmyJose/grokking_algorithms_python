def sum_list(list):
    if list == []:
        return 0
    
    return list[0] + sum_list(list[1:])

def size_list(list):
    if list == []:
        return 0
    
    return 1 + size_list(list[1:])

def max_list(list):
    if list is None:
        raise Exception("Empty list cannot be processed!")

    if len(list) == 1:
        return list[0]
    
    sub_max = max_list(list[1:])
    return list[0] if list[0] > sub_max else sub_max