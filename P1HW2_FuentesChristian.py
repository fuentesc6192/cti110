# Christian Fuentes
# 11/16/2024
# P1HW2
# This program calculates travel expenses
budg = float(input('Enter your budget:'))
dest = input('Enter your travel destination:')
gas = float(input('How much will you spend on gas:'))
acom = float(input('How much for accomodation:'))
food = float(input('How much will you spend on food:'))
expe = float(input('Any additional expenses?:'))
total = budg - gas - acom - food - expe
print('----------Travel Expenses----------')
print('Location: ', dest)
print('Initial Budget: $', budg)
print('Fuel: $', gas)
print('Accomodation: $', acom)
print('Food: $', food)
input()
