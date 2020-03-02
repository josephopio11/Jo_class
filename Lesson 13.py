fruits = ["Apple", "Banana", "Cherry"]
print(fruits)

fruits.append("Mango")
print(fruits)

phonebook = {}
phonebook["John"] = 775635627
phonebook["Jack"] = 703948475
phonebook["Jill"] = 791623509
print(phonebook)

student1 = {
    "name": "Natasha",
    "class": "Year 9",
    "age": 13,
    "height": 120
}
print(student1)

student2 = {
    "name": "Elisha",
    "class": " Year 9",
    "age": 14,
    "height": 146
}

student3 = {
    "name": "Jayden",
    "class": " Year 8",
    "age": 14,
    "height": 136
}

student4 = {
    "name": "Mike",
    "class": " Year 2",
    "age": 14,
    "height": 140
}

print(student1)
print(student2)
print(student3)
print(student4)

del student1["height"]
print(student1)

student2.pop('height')
print(student2)