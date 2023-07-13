# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random

user_input= input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

rock='''

                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\


'''

paper='''

 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   

'''

scissors='''

   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/


'''

values=[rock,paper,scissors]
computer_choose=random.randint(0,2)
user_input=int(user_input)
if(user_input==computer_choose):
    print(values[user_input])
    print("\nComputer Chose\n")
    print(values[computer_choose])
    print("DRAW")
elif user_input==0 and computer_choose==1 or user_input==1 and computer_choose==3 or user_input==3 and computer_choose==1:
    print(values[user_input])
    print("\nComputer Chose\n")
    print(values[computer_choose])
    print("You Lose")
else:
    print(values[user_input])
    print("\nComputer Chose\n")
    print(values[computer_choose])
    print("You Win")


# Output

# What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
# 2
#
#
#    ____
#   / __  ( (__) |___ ___
#   \________,'   """""----....____
#    _______<  () dd       ____----'
#   / __   __`.___-----""""
#  ( (__) |
#   \____/
#
#
#
#
# Computer Chose
#
#
#
#  _ __   __ _ _ __   ___ _ __
# | '_ \ / _` | '_ \ / _ \ '__|
# | |_) | (_| | |_) |  __/ |
# | .__/ \__,_| .__/ \___|_|
# | |         | |
# |_|         |_|
#
#
# You Win
