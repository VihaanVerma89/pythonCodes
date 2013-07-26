def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return 2*(21 - n)

print 'diff21(23): ', diff21(23)
print 'diff21(10): ', diff21(10)
