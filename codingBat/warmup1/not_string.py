def not_string(str):
    stringParts = str.split(" ")
    if stringParts[0] != "not":
        return "not " + str
    else:
        return str

print not_string('candy') 
print not_string('x') 
print not_string('not bad')
