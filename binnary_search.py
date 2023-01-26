def binary_search(list, item):
    # this function does a binary search
    low = 0
    high = len(list) - 1

    while low <= high: # Цикл выполняется пока эта часть не сократится до одного элемента
        mid = int((low + high) / 2)
        guess = mid
        if guess == item:
            return list[mid]
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
