num_of_ints = 0

for count in range(1,11):
    print(count, end=". ")
    num = float(input("Enter your number: "))
    if num == int(num):
        num_of_ints += 1

print('Number of integers is: ', num_of_ints)