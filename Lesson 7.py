def ifstatement():
    print('What is your name?')
    name = input()
    print('Hello ', name)

    print('What is your password')
    password = input()

    if password == 'one':
        print('Password Correct')
    elif password == '1':
        print('Second password correct')
    elif password == 'two':
        print('Third password correct')
    else:
        print('Wrong password')

ifstatement()