phonebook = {
    "John": 775635627,
    "Jack": 703948475,
    "Jill": 791623509
}
print(phonebook)

student1 = {
    "name": "Natasha",
    "class": "Year 9",
    "age": 13,
    "height": 120
}
print(student1)

for x, y in student1.items():
    print(x, ":", y)

phonebook.pop("John")
print(phonebook)

student1.pop('height')
print(student1)

prices = {
    "banana": 500,
    "milk": 1500,
    "chocolate": 7000,
    "apple": 1000,
}

students = ["Edie", "Timothy", "Adrian", "Cassie", "Sarah", "Hero", "Jerry"]
print(students)
students.pop(3)
print(students)
