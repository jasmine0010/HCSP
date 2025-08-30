print("Fibonacci Sequence:")
fib = [1, 1]
for i in range(1, 16):
    fib.append(fib[i - 1] + fib[i])
    print(fib[i])

print("\nSuccessive terms ratio:")
for i in range(1, len(fib)):
    print(fib[i] / fib[i - 1])
print("Limit = 1.618...")