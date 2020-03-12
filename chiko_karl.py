tileArray = ["small black granite", "small grey marble", "small powder blue"]
priceArray = [19.50, 25.95, 35.75]
# area = 0
# boxes = 0
# total_cost = 0
# height = 0
# width = 0
# id_code = 0
# no_of_walls = 0

height = float(input("What's the height in metres?: "))

width = float(input("What's the width in metres?: "))

no_of_walls = int(input("what's the number of walls?: "))

area = height * width
boxes = area / 1

print(
    '''Select any of the available options below
    Enter:
    > 1 for Small black granite, priced at $19.5
    > 2 for Small grey marble, priced at $25.95
    > 3 for Small powder blue, priced at $35.75
    
    '''
)

id_code = int(input("Which tile would you like(1,2 or 3)?: "))
if id_code == 1:
    total_cost = area * 19.50
    print("The total cost is $", total_cost)
    print("The number of boxes you need is", boxes)
    print("The area is", area, "m^2")
elif id_code == 2:
    total_cost = area * 25.95
    print("The total cost is $", total_cost)
    print("The number of boxes you need is", boxes)
    print("The area is", area, "m^2")

elif id_code == 3:
    total_cost = area * 35.75
    print("The total cost is $", total_cost)
    print("The number of boxes you need is", boxes)
    print("The area is", area, "m^2")
else:
    print("invalid")