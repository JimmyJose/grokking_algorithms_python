def sumList(list):
    if list == []:
        return 0
    
    return list[0] + sumList(list[1:])

def sizeList(list):
    if list == []:
        return 0
    
    return 1 + sizeList(list[1:])    