def find_2nd(s):
    idx = s.find('a')
    for i in range(idx + 1, len(s)):
        if s[i] == 'a':
            return i
    return -1

print(find_2nd("banana"))
print(find_2nd("happy birthday"))