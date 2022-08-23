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



#Write your code below this line 👇

def rps(you, computer):
  """0 = rock, 1 = paper, 2 = scissors"""
  if you_choice not in (0, 1, 2):
    print("[ERROR!] Please choose 0, 1, or 2")
    return
  elif you == 0:
    if computer == 0:
      result = "Draw!"
    elif computer == 1:
      result = "You lose"
    else:
      result = "You Win!"
  elif you == 1:
    if computer == 0:
      result = "You Win!"
    elif computer == 1:
      result = "Draw!"
    else:
      result = "You lose"
  else:
    if computer == 0:
      result = "You lose!"
    elif computer == 1:
      result = "You win!"
    else:
      result = "Draw!"

  #print game result
  print (f"You {you_choice}{images_list[you_choice]}\n\n Computer {computer_choice}{images_list[computer_choice]}\n\n {result}")

images_list = [rock, paper, scissors]
you_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
computer_choice = random.randint(0,2)
rps(you_choice, computer_choice)