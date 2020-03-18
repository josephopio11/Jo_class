# Setting up the data storage - Task 1

WeekDay = ["Mon1", "Tue1", "Wed1", "Thu1", "Fri1", "Mon2", "Tue2", "Wed2", "Thu2", "Fri2", "Mon3", "Tue3", "Wed3",
           "Thu3", "Fri3", "Mon4", "Tue4", "Wed4", "Thu4", "Fri4"]
BusA = [0, 0, 0, 2, 2, 4, 0, 3, 4, -2, -5, 0, 0, 3, 4, -1, 8, 1, 1, -2]
BusB = [0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0]
BusC = [2, 0, -1, -1, -2, -2, -3, -1, 0, 0, -2, 0, 1, 1, 1, 1, -1, -1, 2, -2]
BusD = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BusE = [-1, -1, -1, -1, -2, -4, -10, -2, 0, 0, 0, 0, 1, 2, -3, 1, 1, 3, -1, 0, 0]
BusF = [0, -5, -5, -5, -4, -3, -5, 0, 0, 0, 0, -2, -3, 1, 1, 1, 0, 0, -2, -5]
BusIndex = [BusA, BusB, BusC, BusD, BusE, BusF]
BusIndexString = ["BusA", "BusB", "BusC", "BusD", "BusE", "BusF"]

Bus = []
Day = ""


def EnterBusData():
    global Bus
    global Day

    Bus_Choice = str(input("Which bus route would you like to add data to? A,B,C,D,E,F "))
    Day_Choice = int(input("Which day is it? 1: Monday, 2: Tuesday, 3: Wednesday, 4:Thursday, 5:Friday "))
    Week_Choice = int(input("Which week? 1, 2, 3 or 4 "))
    punc = int(input("Enter the number of minutes early or late"))

    if Day_Choice == 1:
        Day = "Mon"
    elif Day_Choice == 2:
        Day = "Tue"
    elif Day_Choice == 3:
        Day = "Wed"
    elif Day_Choice == 4:
        Day = "Thu"
    elif Day_Choice == 5:
        Day = "Fri"

    WeekDay_Choice = Day + str(Week_Choice)

    print("You have selected ", WeekDay_Choice, " Bus route ", "Bus", Bus_Choice)

    for i in range(20):
        if WeekDay_Choice == WeekDay[i]:
            # Case in pseudocode
            if Bus_Choice == "A":
                Bus = BusA
                BusA[i] = int(punc)
            elif Bus_Choice == "B":
                Bus = BusB
                BusB[i] = int(punc)
            elif Bus_Choice == "C":
                BusC[i] = int(punc)
                Bus = BusC
            elif Bus_Choice == "D":
                BusD[i] = int(punc)
                Bus = BusD
            elif Bus_Choice == "E":
                BusE[i] = int(punc)
                Bus = BusE
            elif Bus_Choice == "F":
                BusF[i] = int(punc)
                Bus = BusF
            else:
                Bus = "error"

    print("Bus", Bus_Choice, "on", WeekDay_Choice, "was ", punc, "minutes early/late")


def StatsData():
    global Bus
    global BusIndex
    global BusIndexString

    BusLates = [0, 0, 0, 0, 0, 0]
    BusAverage = [0, 0, 0, 0, 0, 0]
    HighestLates = 0
    HighestLatesBus = ""
    BusAverageLate = [0, 0, 0, 0, 0, 0]

    for i in range(len(BusIndex)):
        Bus = BusIndex[i]
        lateCounter = 0
        TotalLate = 0
        Total = 0
        Average = 0
        AverageLate = 0
        # Find position based on Bus_Choice
        for j in range(len(Bus)):
            if Bus[j] < 0:
                lateCounter = lateCounter + 1  # Counts lates for one bus
                TotalLate = TotalLate + Bus[j]  # Totals late minutes for one bus
            Total = Total + Bus[j]  # Totals all minutes for one bus
        Average = Total / 20  # Calculates average minutes late for one bus
        if lateCounter > 0:
            AverageLate = TotalLate / lateCounter  # calculates the average minutes late only on days late.

        BusLates[i] = lateCounter  # Late counter into BusLates array
        BusAverage[i] = Average  # Places average into BusAverage array
        BusAverageLate[i] = AverageLate  # Places average for late days in BusAverageLateArray

    # Determines highest number of lates for all buses
    for i in range(len(BusLates)):
        if BusLates[i] > HighestLates:
            HighestLatesBus = BusIndexString[i]

    for i in range(len(BusIndex)):
        print("Bus Lates- ", BusIndexString[i], ": ", BusLates[i], "times")
        print("Bus Average- ", BusIndexString[i], ": ", BusAverage[i], "minutes")
        print("Bus Average when Late- ", BusIndexString[i], ": ", BusAverageLate[i], "minutes")
        print("\n")
    print("Highest Lates- ", HighestLatesBus)


def StatsDataByBus():
    global BusIndex
    global BusIndexString
    global WeekDay
    LatesDayCounter = 0

    # Input a specific day
    Day_Choice = int(input("Which day is it? 1: Monday, 2: Tuesday, 3: Wednesday, 4:Thursday, 5:Friday "))
    Week_Choice = int(input("Which week? 1, 2, 3 or 4 "))
    if Day_Choice == 1:
        Day = "Mon"
    elif Day_Choice == 2:
        Day = "Tue"
    elif Day_Choice == 3:
        Day = "Wed"
    elif Day_Choice == 4:
        Day = "Thu"
    elif Day_Choice == 5:
        Day = "Fri"

    WeekDay_Choice = Day + str(Week_Choice)
    print("You have selected ", WeekDay_Choice)

    # How many buses were late on this day

    for i in range(len(WeekDay)):
        if WeekDay[i] == WeekDay_Choice:
            LateDay = i

    for j in range(len(BusIndex)):
        Bus = BusIndex[j]
        if Bus[LateDay] < 0:
            LatesDayCounter = LatesDayCounter + 1

    print(LatesDayCounter, "buses were late on", WeekDay_Choice)

    # For each display the route label and how many minutes late on that day.

    for j in range(len(BusIndex)):
        Bus = BusIndex[j]
        if Bus[LateDay] < 0:
            print(BusIndexString[j], ": ", Bus[LateDay] * -1, " minutes late")


# Main Loop
again = "y"
while again == "y":
    Loop = False
    while Loop == False:
        Choice = int(input(
            "would you like to: 1)enter data, 2)See statistics for all buses or 3)See statistics for a specific day?"))

        if Choice == 1:
            EnterBusData()
            Loop = True
        elif Choice == 2:
            StatsData()
            Loop = True
        elif Choice == 3:
            StatsDataByBus()
            Loop = True
        else:
            Loop = False

    again = input("Do you want to go again? y or n")
    again.lower()