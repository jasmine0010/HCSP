def is_sleeping_hour(hour):
    return hour < 6 or hour > 22

def is_vampire(hour, awake):
    return is_sleeping_hour(hour) and awake or not is_sleeping_hour(hour) and not awake

def test_vampire(hour, awake, expected):
    result = is_vampire(hour, awake)
    print(f"Hour: {hour}, awake: {awake}, expected: {expected}, result: {result}")

    if (expected == result):
        print("PASSED")
    else:
        print("FAILED")

test_vampire(23, True, True)
test_vampire(8, True, False)
test_vampire(14, False, True)