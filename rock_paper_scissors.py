import random
print('===================')
print('Rock Paper Scissors')
print('===================')
print('  1) ✊')
print('  2) ✋')
print('  3) ✌️')
player = int(input('pick a number : '))
computer=random.randint(1,3)
choices = {1: "✊", 2: "✋", 3: "✌️"}
print(f"You chose: {choices[player]}")
print(f"CPU chose: {choices[computer]}")
if player==computer:
    print("It's a tie")
elif player==1 and computer==3:
    print("You lose")
elif player==2 and computer==1:
    print("You lose")
elif player==3 and computer==2:
    print("You lose")
else:
    print("The player won!")