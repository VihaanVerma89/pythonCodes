def make_tags(tag, content):
    return "<"+tag+">"+content+"</"+tag+">"

print make_tags('i','Yay')
print make_tags('i','Hello')
print make_tags('cite','Yay')
