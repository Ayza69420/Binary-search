def binary_search(a, t) -> int:
    l, r = 0, len(a)-1

    while l <= r:
        m=(l+r)//2

        if t == a[m]:
            return m

        elif t < a[m]:
            r -= m-1

        else:
            l += m+1

    return -1

# Example below

array = [1,2,3,4,5]
target = 3

print(binary_search(array, target))
