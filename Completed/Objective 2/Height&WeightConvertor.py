#Write a program to convert a person’s height in inches into centimetres and their weight in stones into kilograms. [1 inch = 2.54 cm and 1 stone = 6.364 kg]

HeightInches = int(input("What is your height in inches? "))
WeightStones = int(input("What is your weight in stones? "))


print("You are ",HeightInches*2.54," cm tall.")
print("You weigh ",WeightStones*6.364," kg.")