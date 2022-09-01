AmountOfLetters = 7
while True:
    word = input(f"Tell me a word with {str(AmountOfLetters)} letters: ")
    if len(word) == AmountOfLetters:
        print(f"Well done! That word has {str(AmountOfLetters)} letters!")
        if AmountOfLetters == 7:
            AmountOfLetters = 4
        else:
            AmountOfLetters = 7
    else:
        print(
            f"Whoops! Your word had {str(len(word))} letter and I was looking for {str(AmountOfLetters)}")
