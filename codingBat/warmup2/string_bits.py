def string_bits(str):
    result = ""
    for i in xrange(len(str)):
        if i % 2 == 0:
            result += str[i]

    return result
print string_bits('Hello') 
print string_bits('Hi')
print string_bits('Heeololeo')

