# statement = 'I love my family They are the best'
#
# print(statement.split()[3])

# class Calculator:
#     def addition(x, y):
#         add = x + y
#         print(add)
#
#     def subtraction(x, y):
#         sub = x - y
#         print(sub)
#
#     def multiplication(x, y):
#         mult = x * y
#         print(mult)
#
#     def division(x, y):
#         div = x / y
#         print(div)
#
#
# Calculator.addition(2, 3)
# Calculator.division(5,4)
# Calculator.multiplication(6,7)
# Calculator.subtraction(6,100)


class Animal:
    legs = int(input('Enter the number of legs'))
    wings = int(input('Enter the number of wings'))


class Car:
    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def accelerate(self):
        pass

    def slow_down(self):
        pass

    def open_window(self):
        pass


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("Tom", "red", 30)

r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()
