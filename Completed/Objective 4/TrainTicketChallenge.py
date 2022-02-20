#A train fare from Cheltenham to London is calculated in the following way:
# £20 per station from start to destination for adults.
# £5 extra per stop between 6am and 9am.
# Half price for children.
#Write a program that allows the user to enter how many stations they need to pass through, how many adults, how many children and the time of day (as a number: 24 hour clock). The program should output the correct fare.

StationsNeeded = int(input("How many stations need to be passed through? "))
Adults = int(input("Number of adults: "))
Children = int(input("Number of children: "))
Time = int(input("What time: (24hrs)"))

if Time >6 and Time < 9:
     print("Price:  £",(Adults*20+Children*10+5)*StationsNeeded)
else:
     print("Price:  £",(Adults*20+Children*10)*StationsNeeded)