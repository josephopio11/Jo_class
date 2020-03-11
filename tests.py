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

# my_string = "The rain is in Spain. Please don't look at me I am so cute"
# print(my_string)
#
# new_string = my_string.split()
# print(new_string)
#
# for i in new_string:
#     print(i)
#
#
# # Declare phonebook dictionary and add values immediately
# phonebook = {
#     "John": 775635627,
#     "Jack": 703948475,
#     "Jill": 791623509
# }
# print(phonebook)


#### fourth session ####

# # this is an array called "col"
# col = ["Apple", "Banana", "Blackberry", "Microsoft"]
#
# # multiply the array by 3 and assign it to new_col
# new_col = col * 3
# # print the new_col array
# print(new_col)
#

# Write all this in one straight line
# kitchen = [['Pineapple','Mango','Banana'],['Rice','Matooke','Potatoes'],['Gas','Charcoal','Oven']]
#
# print(kitchen)

# horsemen = ["war", "famine", "pestilence", "death"]
# children = ["school","fun","study","friends"]
# family = ["love","joy","belonging","belong"]
# statement = "I love my family. They are the best."
#
# everything = [horsemen, children, family]
# print(everything)
#
# new_horsemen = horsemen * 2
# print(new_horsemen)
#
# print(children[2:])
#
# print(family[0:3])
#
# print(statement.split())
#
# q = family + children
# print(q)
#
# print('joy' in family)





# letters = [['a','b','c'],['d','e','f']]
#
# print(letters)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)


# for x in "Ajing Kur":
#     if x == 'g':
#         continue;
#     print(x)
#
# 'banana' in ['apple','banana','microsoft']
#
# print('a' in "microsoft")
# print('l' in 'apple')
# print('y' in 'banana')

# phones = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo', 'LG', 'Motorola']

# for y in phones:
#     print(y)
#     if y == phones[3]:
#         break;


# two = phones[3]
# print(two)
#
# for letter in two:
#     if letter == 'a':
#         continue
#     print(letter)

tiles = {
    'small_black_granite': 19.5,
    'small_grey_marble': 25.95
}

print(tiles['small_black_granite'])