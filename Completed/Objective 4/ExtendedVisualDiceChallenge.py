#Write a program that asks for a number and outputs that number as a graphical dice.

Dice1 = """
oooooooooooo
o          o
o          o
o    #     o
o          o
o          o
oooooooooooo
"""
Dice2 = """
oooooooooooo
o          o
o    #     o
o          o
o    #     o
o          o
oooooooooooo
"""

Dice3 = """
oooooooooooo
o    #     o
o          o
o    #     o
o          o
o    #     o
oooooooooooo
"""

Dice4 = """
oooooooooooo
o          o
o   #   #  o
o          o
o   #   #  o
o          o
oooooooooooo
"""
Dice5 = """
oooooooooooo
o  #    #  o
o          o
o     #    o
o          o
o  #    #  o
oooooooooooo
"""

Dice6 = """
oooooooooooo
o  #    #  o
o          o
o  #    #  o
o          o
o  #    #  o
oooooooooooo
"""

Number = int(input("Side of dice to display (1-6): "))

if Number < 1 or Number > 6:
    print("Invalid number")
elif Number == 1:
    print(Dice1)
elif Number == 2:
    print(Dice2)
elif Number == 3:
    print(Dice3)
elif Number == 4:
    print(Dice4)
elif Number == 5:
    print(Dice5)
elif Number == 6:
    print(Dice6)