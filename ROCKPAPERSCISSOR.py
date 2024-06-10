import random
user_choice = int(input("Enter your choice : Type 0 for Rock, 1 for Paper and 2 for Scissor : ))
 if user_choice > 2 or user_choice < 0:
      print("Invalid choice")
 else:
      computer_choice = print(random.randint(0, 2))
      if user_choice == computer_choice:
          print("It's a tie")
      elif user_choice == 2 and computer_choice == 0:
          print("You Lose")
      elif user_name == 0 and computer_choice == 2:
          print("You Win")
      elif computer_choice > user_choice:
          print("You Lose")
      elif user_choice > computer_choice:
          print("You Win")
