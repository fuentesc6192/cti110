# Christian Fuentes
# 12/3/2024
# P3HW2
# This code calculates hourly pay + possible overtime
empname = input("Enter employee's name:")
hoursworked = float(input('Enter number of hours worked:'))
payrate = float(input("Enter employee's pay rate:"))
if hoursworked > 40:
 
othours = hoursworked - 40
 
otpayrate = payrate * 1.5
 
otpay = othours * otpayrate
 
regpay = payrate * 40
 
gross = regpay + otpay
else :
 
othours = 0
 
otpay = 0
 
regpay = payrate * hoursworked
 
gross = regpay
'''
Legend :
hoursw = Hours Worked
otpayrate = Overtime Pay Rate
otpay = Overtime Pay
othours = Overtime Hours
regpay = Regular Pay
gross = Gross Pay
'''
print('------------------------------------------')
print('Employee name: ', empname)
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print('-------------------------------------------------------------------------------------------------')
print(f'{hoursworked:<15}{payrate:<12}{othours:<12}{otpay:<20}{"$"}{regpay:<20.2f}{"$"}{gross:.2f}')
input()
