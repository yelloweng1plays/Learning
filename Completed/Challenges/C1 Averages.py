Number = []
ContinueValue= True

Number.append(int(input("Enter an initial Number ")))
while ContinueValue:
  Number.append(int(input("Enter a Number ")))
  ContinueValue = int(input("Input '0' for average or input '1' to continue "))

Average=0
for MeanValue in Number:
  Average=Average+MeanValue 
Average=Average / len (Number)
print ("The mean average of ",Number," is ",Average)
