#Write a program that will ask the user to enter the length, depth and height of a fish tank in cm. Calculate the volume of water required to fill the tank and display this volume in litres and UK gallons. To calculate volume in litres, multiply length by depth by height and divide by 1000.
print("Give all answers in Centimetres (CM)")
Length = int(input("Fish tank length: "))
Depth = int(input("Fish tank Depth: "))
Height = int(input("Fish tank length: "))

Answer = Length*Depth*Height

print("The volume in Mililetres: ",Answer/100)
print("Volume in Litres: ",Answer/1000)
