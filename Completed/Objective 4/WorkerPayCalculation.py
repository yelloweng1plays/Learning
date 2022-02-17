#A worker gets paid £9/hour plus £0.60 for every toy car they make in a factory. Write a program that allows the worker to enter the number of hours they have worked and the number of trains they have made. The program should output their wages for the day.

HoursWorked = int(input("How many hours did you work? "))
CarsMade = int(input("How many cars were made? "))

print("You have made £",9*HoursWorked," from hours worked and £",CarsMade*0.6," from making cars. This is a total of £",9*HoursWorked + CarsMade*0.60)

