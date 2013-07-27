def combo_string(str1, str2):
    if len(str1) < len(str2):
        return str1+str2+str1
    else:

        return str2+str1+str2

print combo_string('Hello', 'hi')
print combo_string('hi', 'Hello')
print combo_string('aaa', 'b')


