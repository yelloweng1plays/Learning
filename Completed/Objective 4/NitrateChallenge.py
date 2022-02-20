# When keeping fish, one of the goals to reduce algae is to keep nitrates to a minimum.  One way of doing  this is to dose a carbon source which nitrifying bacteria within an aquarium consume together with  nitrates.  The carbon source has to be dosed very precisely. 

NitrateNumber = float(input("Input the nitrate number: "))

if NitrateNumber > 50 or NitrateNumber < 1:
    print("Invalid number.")
elif NitrateNumber > 10: 
    print("Dose 3ml")
elif NitrateNumber > 2.5:
    print("Dose 2ml")
elif NitrateNumber > 1:
    print("Dose 1ml")
elif NitrateNumber < 1: 
    print("Dose 0.5ml")

