def last2(str):
    if len(str) < 2:
        return 0

    last2 = str[len(str) -2 :]
    count = 0

    for i in range(len(str)-2):
        subString = str[i:i+2]
        if subString == last2 :
            count+=1
    return count


print 'last2('hixxhi') :',last2('hixxhi')  
print 'last2('xaxxaxaxx') :',last2('xaxxaxaxx') 
print 'last2('axxxaaxx') :', last2('axxxaaxx')
