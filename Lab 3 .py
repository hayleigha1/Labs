print("Welcome to the Flarsheim Guesser!")
print()
print("Please think of a number between and including 1 and 100.")
print()

play = True

while play:
        
    remainder_3 = 0
    remainder_3 = True

    while remainder_3:
        user_1 = int(input("What is the remainder when your number is divided by 3 ?"))
        if user_1 < 0:
            print("The value entered must be 0 or greater")
        elif user_1 > 3:
            print("The value entered must be less than 3")
        else:
            print()
            remainder_3 = False
        
    remainder_5 = 0
    remainder_5 = True

    while remainder_5:
        user_2 = int(input("What is the remainder when your number is divided by 5 ?"))
        if user_2 < 0:
            print("The value entered must be 0 or greater")
        elif user_2 > 5:
            print("The value entered must be less than 5")
        else:
            print()
            remainder_5 = False
    
    remainder_7 = 0
    remainder_7 = True
    
    while remainder_7:
        user_3 = int(input("What is the remainder when your number is divided by 7 ?"))
        if user_3 < 0:
            print("The value entered must be 0 or greater")
        elif user_3 > 7:
            print("The value entered must be less than 7")
        else:
            remainder_7 = False
            break

    for i in range (1,101):

        user_num = i

        if (i % 3) == user_1 and (i % 5) == user_2 and (i % 7) == user_3:

            print("Your number was", user_num)
            print("How amazing was that?")

    user = input("Do you want to play again? Y to continue, N to quit ==>")

    if (user == "N"):
        play = False
    
