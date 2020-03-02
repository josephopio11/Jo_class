def grading():
    print('Please enter your mark:')
    mark = int(input())

    if mark >= 70:
        print('A')
    elif mark >= 65:
        print('B')
    elif mark >= 55:
        print('C')
    elif mark >= 50:
        print('D')
    else:
        print('F')

state = True
while state:
    grading()