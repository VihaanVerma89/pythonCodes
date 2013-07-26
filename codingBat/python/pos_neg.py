def pos_neg(a, b, condition):
    if not condition and a*b < 0:
        return  True
    else:
        return  a*b > 0

print pos_neg(1, -1, False) 
print pos_neg(-1, 1, False) 
print pos_neg(-4, -5, True)
