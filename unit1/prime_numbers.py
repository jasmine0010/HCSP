import math

def is_prime(n):
    if n <= 1:
        return False
    if (n == 2):
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def test_prime_numbers(n, expected):
    result = is_prime(n)
    print(f"Number: {n}, expected: {expected}, result: {result}")

    if (expected == result):
        print("PASSED")
    else:
        print("FAILED")

test_prime_numbers(7, True)
test_prime_numbers(16, False)
test_prime_numbers(41, True)