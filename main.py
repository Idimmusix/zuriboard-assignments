
import random
intro = "||ROCK-PAPER-SCISSOR by idimmusix\n||"
rules = '''
RULES:
	 Rock + Paper -> Paper wins
	 Rock + Scissor -> Rock wins
         Paper + Scissor -> Scissor wins
		'''
menu = '''
1. Single Player
2. Two Player
3. Exit
''' #for later when I will include 2 player
rps = ['R', 'P', 'S']
accept = ['1', 'y', 'Y', 'yes', 'Yes', 'YES']

print(intro)

r = input("Do you know the rules (y/n): ")
if r not in accept:
    print(rules)

name = True
while(name):
    pc = '0'
    user = input("choose \nR for Rock\nP for Paper\nS for Scissors\n")
    user = user.upper()
    pc = random.choice(rps)
    if user not in rps:
        print("Invalid input. Try again.")
        continue
    elif user == "R":
        print("Player (Rock): ")
    elif user == "P":
        print("Player (Paper): ")
    else:
        print("Player (Scissors): ")
    if pc == "R":
        print("CPU (Rock)")
    elif pc == "S":
        print("CPU (Scissors)")
    else:
        print("CPU (Paper)")

    if(user == pc):
        print("Draw")
        continue
        
    elif user=='R':
        if pc=='S':
            print("Player won.")
            name=False
            exit(0)
        elif pc=='P':
            print("Player lost.")
            name=False
            exit(0)
    elif user=='P':
        if pc=='S':
            print("Player lost.")
            name=False
            exit(0)
        elif pc=='R':
            print("Player won.")
            name=False
            exit(0)
    elif user=='S':
        if pc=='R':
            print("Player lost.")
            name=False
            exit(0)
        elif pc=='P':
            print("Player won.")
            name=False
            exit(0)
