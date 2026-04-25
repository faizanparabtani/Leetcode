def reverse(x):
    x = str(x)
    x = x[::-1]
    if x[-1] == "-":
        x = x[:-1]
        return int(x.join("-"))
    return int(x.join(""))


x = 123
print(reverse(x))
