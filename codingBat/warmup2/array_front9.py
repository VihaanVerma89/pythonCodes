def array_front9(nums):
    if len(nums) < 4:
        end = len(nums)
    else:
        end = 4

    for i in range(end):
        if nums[i] == 9:
            return True

    return False

print 'array_front9([1, 2, 9, 3, 4]) :',  array_front9([1, 2, 9, 3, 4])
print 'array_front9([1, 2, 3, 4, 9]) :', array_front9([1, 2, 3, 4, 9])
print 'array_front9([1, 2, 3, 4, 5]) :',array_front9([1, 2, 3, 4, 5]) 

