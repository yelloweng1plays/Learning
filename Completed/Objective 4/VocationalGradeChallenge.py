#Write a program that allows you to enter a test mark out of 100.
#The program outputs “FAIL” for a score less than 40, “PASS” for a score of 40 or more, “MERIT” for a
#score of 60 or more and “DISTINCTION” for a score of 80 or more

TestMark = int(input("Input your test mark out of 100: "))

if TestMark < 0 or TestMark > 100:
    print(TestMark," is not a valid test mark.")
elif TestMark >= 80:
    print("Distinction")
elif TestMark >= 60: 
    print("Merit")
elif TestMark >= 40:
    print("Pass")
elif TestMark < 40:
    print("Fail")