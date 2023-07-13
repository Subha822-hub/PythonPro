# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

string_name=name1+name2

string_to_lower=string_name.lower()

t=string_to_lower.count("t")
r=string_to_lower.count("r")
u=string_to_lower.count("u")
e=string_to_lower.count("e")

true=t+r+u+e

l=string_to_lower.count("l")
o=string_to_lower.count("o")
v=string_to_lower.count("v")
e=string_to_lower.count("e")

love=l+o+v+e

true_love=int(str(true)+str(love))

if(true_love<10 or true_love>90):
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif(true_love>40 and true_love<50):
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

# Output

# Welcome to the Love Calculator!
# What is your name?
# Subha
# What is their name?
# Jaisen
# Your score is 21.










