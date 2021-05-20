def findSmallest(arr): 
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: 
            smallest = arr[i] 
            smallest_index = i
    return smallest_index

def sort(arr): 
    if arr is None:
        raise Exception("Cannot sort null or empty array")

    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) 
    return newArr
