class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("Hi my name is " + self.name)


bot_1 = Robot("Tom", "red", 30)
bot_2 = Robot("Jerry", "blue", 40)

bot_1.introduce_self()
bot_2.introduce_self()
