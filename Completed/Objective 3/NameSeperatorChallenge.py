#Write a program that allows the user to enter their full name on one line The program should then outputfor example:
#Forename: Simon
#Surname: Hall
#The program needs to find the space and then extract the characters to the left and right of the space into
#two different variables.


Name = input("Enter your full name: ")
Forename = Name[:Name.find(" ")]
Surname = Name[-Name.find(" "):]
print(Forename)
print(Surname)
