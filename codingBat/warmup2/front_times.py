def front_times(str, times):
    if len(str) > 3:
        return str[:3] * times
    else:
        return str * times

print front_times('Chocolate', 2) 
print front_times('Chocolate', 3)
print front_times('Abc', 3) 

