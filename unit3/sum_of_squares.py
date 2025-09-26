def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

print(sum_of_squares(1))
print(sum_of_squares(2))
print(sum_of_squares(3))