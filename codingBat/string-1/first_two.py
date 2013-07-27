def first_two(string):
    if len(string) < 2 :
        return string
    else:
        return string[:2]

print first_two('Hello') 
print first_two('abcdefg')
print first_two('ab')
