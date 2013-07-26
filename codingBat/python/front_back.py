def front_back(str):
    if len(str) == 1:
        return str
    else:
        return str[len(str)-1] + str[1:len(str)-1]+str[0]


print 'front_back("code") :', front_back('code') 
print 'front_back("a") :', front_back('a') 
print 'front_back("ab") :', front_back('ab') 
