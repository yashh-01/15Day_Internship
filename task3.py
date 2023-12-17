import random

user=input('enter choice (Rock=r,Scissor=s,Paper=p)')
computer=random.choice('r,s,p')

def win(player,opponent):
  if (player=='r' and opponent=='p') or (player=='p' and opponent=='s') or (player=='p' and opponent=='r') :
    return True

if user==computer:
    
    print("it's tie")
elif win(user,computer) :
   print("you won")
else :
   print('you lost')
    