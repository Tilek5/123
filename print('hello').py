ints = int(input('Enter the number of grades: '))
Grades = []
for numbers in range(0, ints):
    NewElement = int(input(f'Enter the {numbers + 1} grade: '))
    Grades.append(NewElement)

A = 0
B = 0
C = 0
D = 0
F = 0

for numbers in range(0, ints):
    if 90 <= Grades[numbers] <= 100:
        A = A + 1
    elif 75 <= Grades[numbers] <= 89:
        B = B + 1
    elif 60 <= Grades[numbers] <= 74:
        C = C + 1
    elif 50 <= Grades[numbers] <= 59:
        D = D + 1
    elif 0 <= Grades[numbers] <= 49:
        F = F + 1

percA = 0
percB = 0
percC = 0
percD = 0
percF = 0

if ints > 0:
    percA = (A / ints) * 100
    percB = (B / ints) * 100
    percC = (C / ints) * 100
    percD = (D / ints) * 100
    percF = (F / ints) * 100

    
print(f'A: {A} grades, ({percA} %)')
print(f'B: {B} grades, ({percB} %)')
print(f'C: {C} grades, ({percC} %)')
print(f'D: {D} grades, ({percD} %)')
print(f'F: {F} grades, ({percF} %)')