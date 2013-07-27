def max_end3(list):
    if list[0]> list[len(list)-1]:
        return list[0:1] * len(list)
    else:
        return list[len(list)-1:] * len(list)

print max_end3([1,2,3])
print max_end3([11,5,9])
print max_end3([2,11,3])
