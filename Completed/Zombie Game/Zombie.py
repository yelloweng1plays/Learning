import time
Scenarios = {
  "Decision1": ["They are coming at us, Which way? left or right? (Left/Right)","left","right","Friend: Really? Left? Ok then","Friend: Really? Right?"],
  "Deision2": ["We can go back and fight or carry on running? (Fight/Run)","fight","run","There are many of them but you get through","You force your way through the locked gate."],
}


def PresentDecision(Username,FriendStatement,Answer1,Answer2,Ans1Response,Ans2Response):
  UserDecision =input("Friend: ",Username," ",FriendStatement)
  if UserDecision.lower() == Answer1.lower():
    print(Ans1Response)
    time.sleep(1)
   
  elif UserDecision.lower() == Answer2.lower():
    print(Ans2Response)
    time.sleep(1)
  else:
    print ("Friend: Wrong decision")
    time.sleep (1)
    PresentDecision(Username,FriendStatement,Answer1,Answer2,Ans1Response,Ans2Response)

def decision2b ():
    print ("Friend: We have to get through that gatebut its locked")
    time.aleep (1)
    dec2b - input ("Friend: Can you jump it or shall we go fight? jump or right")
    if dec2b.lower() == "jump":
         time.sleep (2)
         print ("Friend: You ok "+ user + "? We beat them! ")
   elif dec2b.lower() == "jump":
         time.sleep (2)
         print ("Friend: You done it, now get in!QUICK")
    else:
         print ("Friend: Hurry and make a decision")
         decision2b ()

print ("Welcome to Zombieville!")
print ("Watch out for the walking dead and keep your guard up")
time.sleep (1)
user = input ("Whats your name? ")
time.sleep (1) # delay for 1 second
print ("Run for your life " + user + " and prepare to fight some zombies!")
time.sleep (1)
print ("..... .")
time.sleep (2)
print ("Friend: AAAAARRRGGHHHHHHH RRRRUUUUUUUUUNNNNNNNN")
time.sleep (2)
