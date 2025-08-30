def is_good_deal(original, sale):
    return sale < original * 0.75

def test_good_deal(original, sale, expected):
    result = is_good_deal(original, sale)
    print(f"Original: {original}, sale: {sale}, expected: {expected}, result: {result}")

    if (expected == result):
        print("PASSED")
    else:
        print("FAILED")

test_good_deal(10, 7.5, False)
test_good_deal(15, 11, True)
test_good_deal(34, 30, False)