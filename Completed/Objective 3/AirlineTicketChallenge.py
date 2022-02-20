#Write a program that allows the user to input the name of two cities. The program should then output the
#first 4 characters of each city in capital letters, separated by a dash. For example, London & Madrid would
#be: LOND-MADR



City1 = input("First City: ")
City2 = input("Seccond City: ")

print(City1[:4].upper(),"-",City2[:4].upper())