#Write a program that asks the user to enter the symbol or name of an element, or group it belongs to.  The 
#program should output the name of the element and its atomic weight. 

Elements = {
    "Au":  "Name: Gold, Mass: 197, Group:11",
    "Pb": "Name: Lead, Mass: 207.2, Group:14",
    "Pd": "Name: Palladium, Mass: 106.4, Group:10",
    "K": "Name: Potassium, Mass: 39.1, Group:1",
    "Na": "Name: Sodium, Mass: 23.0 ,Group:1",
    "Fe": "Name: Iron, Mass:55.8, Group:8"
}

import periodictable as ElementsTable


ElementSymbol = input("What is the Symbol of the element:  ")

print(Elements[ElementSymbol])
