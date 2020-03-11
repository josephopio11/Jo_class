wallWidth = 0
wallHeight = 0
wallArea = 0
tileID = 0
tileDescription = ["Small Black granite", "Small Grey Marble", "Small Powder Blue", "medium Sunset Yellow",
                   "Medium Berry Red", "Medium Glitter Purple", "Large Oak Wood Effect", "Large Blck Granite",
                   "Large Bamboo Effect", "Extra-Large White Marble"]
tileIdArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tileBoxPriceArray = [19.5, 25.95, 35.75, 12.5, 11, 52.95, 65, 58.98, 85, 62.75]
tileTotalCost = 0
tileBoxNumber = 0
wallAreaTotal = 0
wastageAllowance = 0
tileWastageIncluded = 0
incompleteEntry = str
for i in range(len(tileIdArray)):
    print(tileDescription[i], "ID: ", tileIdArray[i], " Price per box : $", tileBoxPriceArray[i])

incompleteEntry = input("Would you like to add a wall? (True/False): ")

while incompleteEntry == "True":
    wallWidth = int(input("What is the width of the wall? : "))
    wallHeight = int(input("What is the height of the wall? : "))
    tileID = int(input("What is the ID for the  tile you would like? : "))
    wallArea = wallHeight * wallWidth
    incompleteEntry = input("Would you like to add a wall? (True/False): ")

    wallAreaTotal = wallAreaTotal + wallArea
else:
    tileBoxNumber = wallAreaTotal
    tileTotalCost = tileBoxNumber * (tileBoxPriceArray[tileID - 1])
    print("Wall Area = ", wallAreaTotal)
    print(tileTotalCost, "is the total tile cost without wastage allocation.")
    wastageAllowance = (int(input("Enter a percentage allowance : ")) + 100) / 100
    print(wastageAllowance)
    wastageIncludedBoxNumber = wastageAllowance * tileBoxNumber
    wastageIncludedPrice = wastageIncludedBoxNumber * (tileBoxPriceArray[tileID - 1])

    print("The new number of boxes including wastage allowance is", wastageIncludedBoxNumber,
          " and the new cost price is $", wastageIncludedPrice)
