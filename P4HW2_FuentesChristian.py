# Christian Fuentes
# 12/5/2024
# P4HW2
# This code calculates hourly pay + possible overtime and loops until terminated
'''
Legend :
= = Equal to
!= = Not Equal to
hoursw = Hours Worked
otpayrate = Overtime Pay Rate
otpay = Overtime Pay
othours = Overtime Hours
regpay = Regular Pay
gross = Gross Pay
ottotal = Total Overtime Pay given
regpaytotal = Total Regular Pay given
grosstotal = Total Gross Pay given
emptotal = Total Employees entered
'''
empname = input("Enter employee's name or \"Done\" to terminate:")
ottotal = 0.0
regpaytotal = 0.0
grosstotal = 0.0
emptotal = 0
while empname != "Done":
 
emptotal +=1
 
hoursworked = float(input('Enter number of hours worked:'))
 
payrate = float(input("Enter employee's pay rate:"))
 
if hoursworked > 40:
 
othours = hoursworked - 40
 
otpayrate = payrate * 1.5
 
otpay = othours * otpayrate
 
ottotal += otpay
 
regpay = payrate * 40
 
regpaytotal += regpay
 
gross = regpay + otpay
 
grosstotal += gross
 
 
else : 
 
othours = 0
 
otpay = 0
 
regpay = payrate * hoursworked
 
gross = regpay
 
 
ottotal += otpay
 
regpaytotal += regpay
 
grosstotal += gross
 
print('------------------------------------------')
 
print('Employee name: ', empname)
 
print()
 
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
 
print('-------------------------------------------------------------------------------------------------')
 
print(f'{hoursworked:<15}{payrate:<12}{othours:<12}{otpay:<20}{"$"}{regpay:<20.2f}{"$"}{gross:.2f}')
 
print()
 
 
empname = input("Enter next employee's name or \"Done\" to terminate:")
 
#loop Ends Here
 
print('Total number of employees entered: ', emptotal)
print(f'{"Total amount paid for overtime: $"}{ottotal}')
print(f'{"Total amount paid for regular hours: $"}{regpaytotal}')
print(f'{"Total amount paid in gross: $"}{grosstotal}')
input('Press Enter to Terminate')
