import random

students = [ 
    'Ryan', 'Marcos', 'Shahood', 'Aidan', 'Muntag', 'Chris', 'Gavin', 'Leo', 'Mason', 
    'Jaiden', 'Nate', 'Jackson', 'Asher', 'Jacob', 'Carrell', 'Devin', 'LeBron', 
    'Saquon', 'Jalen', 'Nick'
]

print("Students:")
print(str(students))

# Ensure valid group size input (2, 3, or 4)
while True:
    userInput = input("Choose the number of students in each group (2, 3, 4): ")
    if userInput in ['2', '3', '4']:
        group_size = int(userInput)
        break
    else:
        print("That is not a valid input. Please try again.")

# Handle exclusion of pairs
excluded_pairs = []
for _ in range(2):  # Limit to two pairs
    while True:
        anyExclusions = input("Enter a pair of students that can't work together? (Y/N): ").strip().upper()
        if anyExclusions in ['Y', 'N']:
            break
        print("Invalid input. Please enter Y or N.")
    
    if anyExclusions == 'N':
        break

    while True:
        excludedStudent1 = input("Please enter the name of the first student: ").strip().capitalize()
        if excludedStudent1 in students:
            break
        print('Invalid name. Please try again.')
    
    while True:
        excludedStudent2 = input("Please enter the name of the second student: ").strip().capitalize()
        if excludedStudent2 in students and excludedStudent2 != excludedStudent1:
            break
        print('Invalid name or duplicate entry. Please try again.')
    
    excluded_pairs.append((excludedStudent1, excludedStudent2))

# Generate valid groups
while True:
    random.shuffle(students)
    groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]
    
    # Adjust groups if group size is 3 and one student is left over
    remainder = len(students) % group_size
    if remainder == 1 and group_size == 3:
        # Move the last student into an existing group
        groups[-2].append(groups[-1][0])
        groups.pop()
    
    # Ensure all groups are valid
    valid = True
    for group in groups:
        for pair in excluded_pairs:
            if pair[0] in group and pair[1] in group:
                valid = False
                break
        if not valid:
            break
    
    if valid:
        for group in groups:
            print(group)
        break
