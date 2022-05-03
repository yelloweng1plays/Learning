# Generate Number 	✓
# 4 Digit number input ✓
# Attempts Counter ✓
# Numbers Correct ✓

import random

Attempts = 0
Active = True
RandomNumber = str(random.randint(1000,9999))
print(RandomNumber)
UserNumber = "0000"
CorrectNumbers = 0

while UserNumber != RandomNumber:    
  UserNumber = input("I'm thinking of a number with 4 digits. What do you think it is? ")
  for index in range(len(UserNumber)):
    if UserNumber[index] == RandomNumber[index]:
      CorrectNumbers = CorrectNumbers+1
  print(CorrectNumbers, " correct digits.")
  CorrectNumbers = 0
  Attempts = Attempts+1
  


print("Congratulations! You have guessed the number was ",RandomNumber," it took ",Attempts," attempts.")


