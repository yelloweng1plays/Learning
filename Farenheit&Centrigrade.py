WhatFrom = input("Convert from Centrigrade or Farenheit (C/F)?")

if WhatFrom == "F" or WhatFrom == "f":
  Farenheit = int(input("What is the temperature in °F ? "))
  Centigrade = Farenheit-32*5/9
  print("The temperature in °C is: ", Centigrade)
elif WhatFrom == "C" or WhatFrom == "c":
    Farenheit = int(input("What is the temperature in °F ? "))
    Farenheit = Centigrade+32*5/9
    print("The temperature in °C is: ", Centigrade)






