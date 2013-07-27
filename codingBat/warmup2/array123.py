def array123(nums):
    array123 = [ 1, 2 ,3 ]

    for i in range(len(nums)-2):
        subArray = nums[i:i+3]
        if array123 == subArray :
            return True
    return False
            
print 'array123([1, 1, 2, 3, 1]) :', array123([1, 1, 2, 3, 1])
print 'array123([1, 1, 2, 4, 1]) :', array123([1, 1, 2, 4, 1]) 
print 'array123([1, 1, 2, 1, 2, 3]) :', array123([1, 1, 2, 1, 2, 3]) 
