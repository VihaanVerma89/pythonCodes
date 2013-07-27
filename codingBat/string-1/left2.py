def left2(string):
    if len(string) < 2 :
        return string
    else:
        return string[2:]+string[:2]

print left2('Hello')
print left2('java')
print left2('hi')
