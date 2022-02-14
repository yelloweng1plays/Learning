#Write a program to display the larger of two numbers entered

from nntplib import NNTP
from tkinter import N


Num1 = int(input("Input first Number: "))
Num2 = int(input("Input seccond number: "))

if Num1 > Num2: 
    print("The largest number is number 1")
elif Num1 < Num2: 
    print("The largest number is number 2")