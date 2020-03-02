def calculate(number):
    new_number = number/100
    return new_number


for x in range(5, 101, 5):
    y = calculate(x)
    print(x, "% =", y)
    print("For shizzle")
