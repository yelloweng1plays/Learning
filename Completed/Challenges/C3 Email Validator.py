Active = True
RequiredCharactersInputted = 0
ForbiddenCharacters = {
    " ", '£', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '<', '>', '?', '/', ';', ':', '[', ']', '{', '}', '#', '~', '!', '`', '¬'
}

RequiredCharacters = {
    "@"
}


EmailAddress = input("Enter your email address: ").lower()

print(EmailAddress)

while Active:
    for EmailIndex in EmailAddress:
        for ForbiddenIndex in ForbiddenCharacters:
            if EmailAddress[EmailIndex] == ForbiddenIndex:
                print(ForbiddenIndex, " is forbidden.")
                break
            elif EmailAddress[EmailIndex] == RequiredCharacters:
                RequiredCharactersInputted = RequiredCharactersInputted + 1
            elif RequiredCharactersInputted >= len(RequiredCharacters):
                print("Thank you for inputting your email address (", EmailAddress, ")")
                Active = False
