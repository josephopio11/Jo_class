# mylist = ['name',2,'child',['like','hate','wonder','bike',['Uganda','Kenya','Tanzania']]]
#
# for h in mylist[3][4]:
#     print(h)

# second_list = ['more','less','everything']
#
# print('what' in second_list)
#
# third_list = second_list[1:3]
# print(third_list)
#
# fourth_list = third_list * 3
# print(fourth_list)
#
# fifth_list = fourth_list[2:]
# print(fifth_list)

#####SECOND SESSION#####
# def is_prime(x):
#     # only positive numbers are allowed and the smallest prime number is 2
#     if x > 1:
#         # since the smallest prime number is 2, we start the divisor at 3
#         divisor = 2
#
#         # because the submit number can always be divided by itself we can use the
#         # range function to set the correct range
#         for i in range(divisor, x):
#             if (x % i) == 0:
#                 return False
#     else:
#         return False
#     return True
#
#
# def primes_less_than(n):
#     """ Return a list of all prime numbers less than n. """
#     result = []
#     for i in range(2, n):
#         if is_prime(i):
#             result.append(i)
#     return result
#
#
# x = int(input('Enter the last number: '))
# y = primes_less_than(x)
#
# count = 0
#
# for j in y:
#     count += 1
#
# print(y)
# print(count)


#### THIRD SESSION ####

my_string = "The rain is in Spain. Please don't look at me I am so cute"
print(my_string)

new_string = my_string.split()
print(new_string)

for i in new_string:
    print(i)


# Declare phonebook dictionary
phonebook = {}
# Add "John" with telephone number "775635627" to the dictionary
phonebook["John"] = 775635627
# Add "Jack" with telephone number "703948475" to the dictionary
phonebook["Jack"] = 703948475
# Add "Jill" with telephone number "791623509" to the dictionary
phonebook["Jill"] = 791623509
# Print phonebook to the screen
print(phonebook)


