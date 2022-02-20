#Write a program  to ask for a person’s forename and surname, outputting their
#first initial and the rest of their name in capitals

Forename = input("What is your forename: ")
Surname = input("Surname: ")

print(Forename[:1].upper(),".",Surname.upper())