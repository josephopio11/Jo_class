# year_11 = ["Mikka", "Mary", "Kami", "Chiko", "Sonia", "Karl", "Treasure", "Tracy"]
#
# position = 0
# position = int(input("Enter the array position you would like to see: "))
# print(year_11[position])


students = []

for i in range(8):
    print("Enter the name",end=': ')
    name = input()
    students.append(name)

print(students)

print('''Here is the output of everything in the array
each of the values has been printed in a seperate line   ''')

for count in range(8):
    print(count,end=': ')
    print(students[count])