def binarySearch(array, target) -> int:
    left, right = 0, len(array)-1

    while left <= right:
        middle = (left+right)//2

        if array[middle] == target:
            return middle

        elif array[middle] < target:
            left = middle+1

        else:
            right = middle-1

    return -1
