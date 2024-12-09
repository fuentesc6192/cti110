print('-----Calculating Exponenets----')

print('Enter an interger as the base value:', end='')
basevalue = int(input())
print('Enter an interger as the exponent:', end='')
exponent = int(input())

solution = basevalue**exponent

print(basevalue, 'raised to the power of', exponent, 'is', solution, '!!')

print('-----Addition and Subtraction----')

print('Enter a starting interger:', end='')
starint = int(input())
print('Enter an interger to add:', end='')
addint = int(input())
print('Enter an interger to subtract:', end='')
subint = int(input())

sol = starint+addint-subint

print(starint, '+', addint, '-', subint, 'is equal to', sol)

input('Press ENTER to exit')
