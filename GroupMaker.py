import random

students = [ 
    'Ryan', 'Marcos', 'Shahood', 'Aidan', 'Muntag', 'Chris', 'Gavin', 'Leo', 'Mason', 
    'Jaiden', 'Nate', 'Jackson', 'Asher', 'Jacob', 'Carrell', 'Devin', 'LeBron', 
    'Saquon', 'Jalen', 'Nick'
]


userInput = input("Choose the number of students in each group (2, 3, 4): ")

if userInput ==  '2':
    random.shuffle(students)
    groupsof2 = [students[i:i + 2] for i in range(0, len(students), 2)]
    for groups in groupsof2:
        print(groups)


elif userInput == '3':
    random.shuffle(students)
    groupsof3 = [students[i:i + 3] for i in range(0, len(students), 3)]
    for groups in groupsof3:
        print(groups)


elif userInput == '4':
    random.shuffle(students)
    groupsof4 = [students[i:i + 4] for i in range(0, len(students), 4)]
    for groups in groupsof4:
        print(groups)


else:
    print('That is not a valid input. Please try again.')







