def string_splosion(str):
    result = ""
    for i in xrange(len(str)):
        result += str[ :i+1] 

    return result

print string_splosion('Code')
print string_splosion('abc')
print string_splosion('ab') 
