# Christian Fuentes
# 11/16/2024
# P1HW2
# This program calculates travel expenses
budg = float(input('Enter your budget:'))
print()
dest = input('Enter your travel destination:')
print()
gas = float(input('How much will you spend on gas:'))
print()
acom = float(input('How much for accomodation:'))
print()
food = float(input('How much will you spend on food:'))
print()
expe = float(input('Any additional expenses?:'))
total = budg - gas - acom - food - expe
print()

print('----------Travel Expenses----------')
print('Location:            ',dest)
print(f'{"Initial Budget:       $"}{budg:.2f}')
print(f'{"Fuel:                 $"}{gas:.2f}')
print(f'{"Accomodation:         $"}{acom:.2f}')
print(f'{"Food:                 $"}{food:.2f}')
print('-----------------------------------')
print()
print(f'{"Remaining Balance:    $"}{total:.2f}')
input()
