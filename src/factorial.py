def compute(number):
    if number < 0:
        raise Exception("Negative numbers are not allowed!")

    # The base case
    if number == 0:
        return 1
    
    # The recursive case
    return number * compute(number - 1)
