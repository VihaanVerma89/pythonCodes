def string_match(string1, string2):
    count = 0
    shorter = min(len(string1), len(string2))

    for i in range(shorter - 1) :
        sub1 = string1[i:i+2]
        sub2 = string2[i:i+2]

        if sub1 == sub2 :
            count += 1
    return count
print string_match('xxcaazz', 'xxbaaz') 
print string_match('abc', 'abc') 
print string_match('abc', 'axc')

