import random

user_score=0
computer_score=0

options=["stone", "paper", "scissors"]

while(True):
    user_input=input("Enter stone/paper/scissors or press Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        print("Invalid option.")
        continue

    random_num=random.randint(0,2)
    computer_input=options[random_num]
    print("Computer picked", computer_input +".")

    if user_input==computer_input:
        print("Clash...! Another turn!")
    elif user_input=="stone" and computer_input=="scissors":
        print("You win!")
        user_score+=1
    elif user_input=="paper" and computer_input=="stone":
        print("You win!")
        user_score+=1
    elif user_input=="scissors" and computer_input=="paper":
        print("You win!")
        user_score+=1
    else:
        print("You lose!")
        computer_score+=1
        
print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
if(user_score>computer_score):
    print("You are the winner!")
elif(user_score!=0 and computer_score!=0 and user_score==computer_score):
    print("It's a clash...Good play though!")
else:
    print("Better luck next time. Goodbye!")

