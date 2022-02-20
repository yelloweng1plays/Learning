#A cash machine dispenses £10 and £20 notes to a maximum of £250.  Write a program that shows the user  their balance, asks them how much to withdraw, ensures this is a valid amount without going overdrawn 
#and with the notes available and outputs the new balance.

Balance = 87653

print("Your current balance is: ",Balance)
Withdrawn = int(input("How much do you wish to withdraw? "))

if Balance-Withdrawn > 0 and not Withdrawn > 250:
    if  float(Withdrawn/20).is_integer():
        print("You can have this amount in either ",Withdrawn/20," £20 notes or in ",Withdrawn/10," £10 notes")
        print("Your remaining balance will be ",Balance-Withdrawn)
    elif float(Withdrawn/10).is_integer():
         print("You can have this amount in ",Withdrawn/10," £10 notes")
         print("Your remaining balance will be ",Balance-Withdrawn)
    else:
        print("This machine is only capable of dispensing in £10 and £20 notes")
else:
    print("More than £250 cannot be withdrawn at a time and amount to withdraw must be more than 0")
