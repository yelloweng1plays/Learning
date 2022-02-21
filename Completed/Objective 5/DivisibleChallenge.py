Input1 = int(input("Input 1: "))
Input2 = int(input("Input 2: "))

if float(Input1/Input2).is_integer():
  print(Input1," is exactly divisible by ",Input2)
elif not float(Input1/Input2).is_integer():
  Amount,Remainder = divmod(Input1, Input2)
  print(Input2," goes into ",Input1," ",Amount," times with a remainder of ",Remainder)
elif Input1 <=0:
  print("You cant divide by 0")