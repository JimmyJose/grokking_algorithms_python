def search(item, item_list):
    if item is None:
        raise Exception("No item to search!")

    if item_list is None:
        raise Exception("No list to search against!")

    low = 0
    high = len(item_list)

    while low <= high:
        mid = low + high // 2
        guess = item_list[mid]

        if guess == item:
            return mid

        if guess < item:
            low = mid + 1
        else:
            high = mid - 1 
