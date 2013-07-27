def rotate_left3(arr):
    return arr[1:] + arr[:1]

print rotate_left3([1, 2, 3]) 
print rotate_left3([5, 11, 9])
print rotate_left3([7, 0, 0])

