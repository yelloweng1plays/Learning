#Write a program that asks for your age. If you are over 18 it outputs the message, “Over 18”, otherwise it outputs, “Under 18”


UserAge = int(input("Input your age: "))
if UserAge >= 18:
    print("Over 18")
else:
    print("Under 18")