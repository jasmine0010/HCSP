def attention(str):
    if (str[:8] == "Hey you!"):
        return True
    return False

print(attention("Hello, my name is Inigo Montoya."))
print(attention("Excuse me, Dr. Kessner?"))
print(attention("Hey you! Give me your code!"))