import random

students = [ 
    'Ryan', 'Marcos', 'Shahood', 'Aidan', 'Muntag', 'Chris', 'Gavin', 'Leo', 'Mason', 
    'Jaiden', 'Nate', 'Jackson', 'Asher', 'Jacob', 'Carrell', 'Devin', 'LeBron', 
    'Saquon', 'Jalen', 'Nick'
]

print("Students:")
print(str(students))

userInput = input("Choose the number of students in each group (2, 3, 4): ")

anyExclusions1 = input("Is there any pairs of students that can't work together? Y/N: ")

anyExclusions1 = anyExclusions1.capitalize()

while True:
    if anyExclusions1 == 'Y':
    
        while True:
            excludedStudent1 = input("Please enter the name of the first student: ")
            excludedStudent1 = excludedStudent1.capitalize()
            if excludedStudent1 in students:
                break
            else:
                print('Invalid name. Please try again.')
            
        while True:
            excludedStudent2 = input("Please enter the name of the second student: ")
            excludedStudent2 = excludedStudent2.capitalize()
            if excludedStudent2 in students:
                break
            else:
                print('Invalid name. Please try again.')
                
                
        anyExclusions2 = input("Is there another pair of Students that cannot work together? Y/N: ")

        anyExclusions2 = anyExclusions2.capitalize()
            
    elif anyExclusions1 == 'N':
        break

    else:
        print("That's an invalid input. Please try again.")
        




while True:
    if userInput == '2':
        random.shuffle(students)
        groupsof2 = [students[i:i + 2] for i in range(0, len(students), 2)]
        for groups in groupsof2:
            print(groups)
        break

    elif userInput == '3':
        random.shuffle(students)
        groupsof3 = [students[i:i + 3] for i in range(0, len(students), 3)]
        for groups in groupsof3:
            print(groups)
        break

    elif userInput == '4':
        random.shuffle(students)
        groupsof4 = [students[i:i + 4] for i in range(0, len(students), 4)]
        for groups in groupsof4:
            print(groups)
        break

    else:
        print('That is not a valid input. Please try again')
        userInput = input("Choose the number of students in each group (2, 3, 4): ")
