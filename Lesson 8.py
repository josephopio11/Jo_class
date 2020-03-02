def nested_if():
    print('Enter the mark you scored')
    mark = int(input())

    if mark >= 70:
        print('You excelled')
    elif mark >= 50:
        print('You passed')
    else:
        print('You failed')

nested_if()
