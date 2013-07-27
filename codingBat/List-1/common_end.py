def common_end(arr1, arr2):

    return (arr1[1] == arr2[1] or arr1[len(arr1)-1] ==arr2[len(arr2)-1])

print common_end([1, 2, 3], [7, 3])
print common_end([1, 2, 3], [7, 3, 2])
print common_end([1, 2, 3], [1, 3])
