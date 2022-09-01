pi = 3.142

ABDistance = float(input("Input straight line distance between points A and B: (Miles)"))

ABDistanceKM = ABDistance*1.6

Circumference = pi*ABDistanceKM

FlightpathDistance = Circumference/2

print("Distance between satelites is: ",int(FlightpathDistance))