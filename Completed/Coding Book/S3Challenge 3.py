import random

AnimalNames = [
    "Elephant",
    "Giraffe",
    "Penguin",
    "Bearded Dragon"
]

SelectedWord = random.choice(AnimalNames)

print(
    f"I'm thinking of an animal begining with {SelectedWord[0:1]} and ending with {SelectedWord[-1]}")

Guess = input("What animal am I thinking of? ")
if Guess == SelectedWord:
    print("Correct!")
else:
    print("Incorrect")
