def count_occurrences(str, sub):
    cnt = 0
    for i in range(len(str) - len(sub) + 1):
        cnt += str[i:i+len(sub)] == sub
    return cnt

print(count_occurrences("Mississippi", "iss"))
print(count_occurrences("banananana", "na"))
print(count_occurrences("hello", "lo"))