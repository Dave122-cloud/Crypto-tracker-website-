import random

user_choice= int(input("what is your choice?type 0 for rock 1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid choice")

elif user_choice == 0 and computer_choice== 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")

elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
if user_choice == computer_choice:
    print("draw")
    if user_choice>= 3 or user_choice < 0:
        print("you typed an invalid choice")


