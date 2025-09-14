import random
running = True
nums = ["1", "2", "3", "4", "5", "6"]
while running:
    print("D6 Dice:")
    user_input = input("you want to roll(yes/no):")
    if user_input == "yes":
        dice_roll = random.choice(nums)
        print()
        print('you rolled:' + dice_roll)
        print()
    elif user_input == "no":
        running = False