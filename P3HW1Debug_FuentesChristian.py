# Christian Fuentes
# 12/3/24
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules
'''
mod_1 = input('Enter grade for Module 1: ')
 mod_2 = input('Enter grade for Module 2: ')
mod_1 = input('Enter grade for Module 3: )
mod 4 = input('Enter grade for Module 1: ')
mod_1 = input('Enter grade for Module 5: ')
 mod_1 = input('Enter grade for Module 6: ")
'''
mod1 = float(input('Enter grade for module 1:'))
mod2 = float(input('Enter grade for module 2:'))
mod3 = float(input('Enter grade for module 3:'))
mod4 = float(input('Enter grade for module 4:'))
mod5 = float(input('Enter grade for module 5:'))
mod6 = float(input('Enter grade for module 6:'))
# add grades entered to a list
grades = [mod1,mod2,mod3,mod4,mod5]
# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades)/ len(grades)
# determine letter grade for average
'''
if avg >= 90:
print('Your grade is: A')
else:
if average > 80:
 print('Your grade is: B')
else:
else:
print('Your grade is: F') # TO DO: finish this
'''
print()
print('------------Results------------')
print('Lowest Grade: ', low)
print('Highest Grade: ', high)
print('Sum of Grades: ', total)
print(f"{'Average: '} {avg:.2f}")
print('-----------------------------------------')
if avg >= 90:
 
print('Your grade is: A')
elif avg >= 80:
 
print('Your grade is: B')
elif avg >= 70:
 
print('Your grade is: C')
elif avg >= 60:
 
print('Your grade is: D')
else :
 
print('Your grade is: F')
input()
