import time
Alphabet = "abcdefghijklmnopqrstuvwxyz"

WhatIveBought = []

print("I went to the market and bought")
time.sleep(0.1)
for x in Alphabet:
    Item = input(f"Enter an item starting with '{x}':")
    WhatIveBought.append(Item+" and a ")
    print("I went to the market today and bought an ",WhatIveBought)