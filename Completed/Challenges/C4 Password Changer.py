from getpass4 import getpass

debug = True

Password1 = getpass("Input new password: ") 
print("Please confirm your password")
Password2 = getpass("Input new password: ")

if debug: print("Pass1: ",Password1," Pass2: ",Password2)

if Password1 == Password2:
    if Password1.islower():
        print("Your password must contain at least 1 uppercase and 1 lowercase letter")
    elif Password1.isupper():
        print("Your password must contain at least 1 uppercase and 1 lowercase letter")
    else:
        print("Congratulations your new password has been set!")
else:
    print("Error: Your passwords do not match!")