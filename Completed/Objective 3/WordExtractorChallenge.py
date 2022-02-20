#Write a program that outputs the sentence: Quick brown fox jumps over the lazy dog. The user can then
#enter the word to be cut from the sentence. The sentence is then output with the word removed.

Text = "The quick brown fox jumps over the lazy dog."
print(Text)
WordToRemove = input("Which word do you wish to remove from the previous sentence: ")
AlteredText = Text.replace(WordToRemove, "")
print(AlteredText)