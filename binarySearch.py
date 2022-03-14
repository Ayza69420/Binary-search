def binary_search(li, tar) -> int:
    l, r = 0, len(li)-1

    while l <= r:
        m=(l+r)//2

        if tar == li[m]:
            return m

        elif tar < li[m]:
            r -= m-1

        else:
            l += m+1

    return -1

# Example below

array = [1,2,3,4,5]
target = 3

print(binary_search(array, target))
