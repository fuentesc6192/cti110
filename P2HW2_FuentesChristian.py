# Christian Fuentes
# 11/26/2024
# P2HW2
# This program takes inputted grades and averages them out
mod1 = float(input('Enter grade for module 1:'))
mod2 = float(input('Enter grade for module 2:'))
mod3 = float(input('Enter grade for module 3:'))
mod4 = float(input('Enter grade for module 4:'))
mod5 = float(input('Enter grade for module 5:'))
mod6 = float(input('Enter grade for module 6:'))
grades = [mod1,mod2,mod3,mod4,mod5,mod6]
low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades)/ len(grades)
print()
print('------------Results------------')
print('Lowest Grade: 
', low)
print('Highest Grade: 
', high)
print('Sum of Grades: 
', total)
print(f"{'Average: 
'} {avg:.2f}")
print('-----------------------------------------')
input()
