def make_out_word(pattern, word):
    return pattern[:2]+word+pattern[2:]


print make_out_word('<<>>', 'Yay') 
print make_out_word('<<>>', 'WooHoo')
print make_out_word('[[]]', 'word') 
