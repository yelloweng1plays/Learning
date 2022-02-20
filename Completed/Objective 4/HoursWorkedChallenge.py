#Write a program that asks the user for the number of hours worked this week and their hourly rate of pay.
#The program is to calculate the gross pay. If the number of hours worked is greater than 40, the extra hours are paid at 1.5 times the rate. The program should display an error message if the number of hours worked is not in the range 0 to 60.

HoursWorked = float(input("Hours worked this week: "))
HourlyRate = float(input("Hourly rate: "))

if HoursWorked < 1 or HoursWorked > 60:
    print("Error")
else:
    if HoursWorked > 40:
        print("Your gross pay is: £",HourlyRate*HoursWorked*1.5)
    else:
        print("Your gross pay is: £",HourlyRate*HoursWorked)