def interlace(a, b):
    s = ""
    for i in range(min(len(a), len(b))):
        s += a[i] + b[i]
    if (len(a) > len(b)):
        s += a[len(b):]
    elif (len(b) > len(a)):
        s += b[len(a):]
    return s

print(interlace("abc", "123"))
print(interlace("bed", "ras"))
print(interlace("hello", "goodbye"))