def binarySearch(array,target)
    left,right=0,array.size-1

    until left > right
        middle=((left+right)/2).round
        return middle if array[middle] == target
        array[middle]<target ? left=middle+1 : right=middle-1
    end

    return -1
end
