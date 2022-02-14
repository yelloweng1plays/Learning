#Write a program that reads in the temperature of water in a container in Centigrade and displays a
#message stating whether the water is frozen (zero or below), boiling (100 or greater) or neither.

WaterTemperature = int(input("Input water temperature in c°: "))

if WaterTemperature <= 0:
    print("Water temperature is freezing.")
elif WaterTemperature >= 100:
    print("Water temperature is boiling.")
else:
    print("Water is neither boiling nor freezing.")