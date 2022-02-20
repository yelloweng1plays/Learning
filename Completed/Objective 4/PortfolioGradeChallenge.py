#Write a program that inputs a mark from the keyboard for sections of a project: ‘analysis’, ‘design’, ‘implementation’ and ‘evaluation’.  The program should output the total mark, the grade, and how many 
#more marks were needed to get into the next mark band. 
 
#Grades are: 
#  0 U 
#  4 G 
#  13 F 
#  22 E 
#  31 D 
#  41 C 
#  54 B 
#  67 A 
#  80 A*

Analysis = int(input("What was the mark for Analysis "))
Design = int(input("What was the mark for Design "))
Implementation = int(input("What was the mark for Implementation "))
Evaluation = int(input("What was the mark for Evaluation "))


Grade = Analysis+Design+Implementation+Evaluation

if Grade >= 80:
    print("Grade is A*")
elif  Grade >= 67:
    print("Grade is A, Marks needed for next grade: 13")
elif Grade >= 54:
    print("Grade is B, Marks needed for next grade: 23")
elif Grade >= 41:
    print("Grade is C, Marks needed for next grade: 13")
elif Grade >= 31:
    print("Grade is D, Marks needed for next grade: 10")
elif Grade >= 22:
    print("Grade is E, Marks needed for next grade: 9")
elif Grade >= 13:
    print("Grade is F, Marks needed for next grade: 9")
elif Grade >= 4: 
    print("Grade is G, Marks needed for next grade: 9")
elif Grade >= 0:
    print("Grade is U, Marks needed for next grade: 4")