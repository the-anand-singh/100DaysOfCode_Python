import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ['rock', 'paper', 'scissors']
option_images = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))



if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")

else:
    print(option_images[user_choice])

    print('Computer chose:')
    computer_choice = random.randint(0, 2)
    print(option_images[computer_choice])

    if user_choice == computer_choice:
        print('It\'s a draw')
    elif computer_choice - 1 == user_choice % 2:
        print('You lose')
    else:
        print('You win')


