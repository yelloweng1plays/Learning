#Write a program that:
#• Asks the user to enter the diameter of a circle.
#• Outputs the radius of the circle (diameter divided by 2)
#• Outputs the area of the circle (3.14 multiplied by the radius squared)
#• Outputs the circumference of the circle (3.14 multiplied by the diameter)
#• Asks the user to enter the arc angle
#• Outputs the arc length (circumference multiplied by the arc angle, divided by 360)


Diameter = float(input("Enter the diameter of the circle: "))
ArcAngle = float(input("Enter arc angle: "))
print(
    "Circle Radius: ",Diameter/2,
    "Area of circle: ",(Diameter/2)**2 *3.14,
    "Circumference of circle: ",3.14*Diameter,
    "Arc length ",(3.14*Diameter)*ArcAngle/360
)