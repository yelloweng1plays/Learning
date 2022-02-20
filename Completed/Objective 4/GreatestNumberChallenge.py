#Write a program to display the larger of two numbers entered

Num1 = float(input("What is your first number to compare?"))
Num2 = float(input("What is the seccond number to compare?"))

if Num1 > Num2:
    print("Number 1: ",Num1," is greater than Number 2: ",Num2)
elif Num1 < Num2: 
    print("Number 1: ",Num1," is smaller than Number 2: ",Num2)
else:
    print("Error: invalid or same numbers")