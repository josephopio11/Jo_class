foods = ['fish','chocolate','cake','chicken','grapes','olives','raisins','carrots','bananas']

while True:
    print('Guess the food Tracy loves: ',end='')
    x = input()
    if x in foods:
        print('You are right, she loves',x,end='. ')
        print('It is located in position ', foods.index(x),'of her likes')
    else:
        print('No, way! Please try again')