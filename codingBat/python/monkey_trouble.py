def monkey_trouble(a_smile, b_smile):
    return ((a_smile and b_smile) or (not a_smile and not b_smile))

print monkey_trouble(True, True)
print monkey_trouble(False, False)
print monkey_trouble(True, False)


