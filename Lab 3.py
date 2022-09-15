print("Welcome to the Flarsheim Guesser!")
print()
print("Please think of a number between and including 1 and 100.")
print()

play = True

while play:

    for i in range (1,101):
        
        remainder_3 = 0
        remainder_3 = True

        while remainder_3:
            remainder_3 = int(input("What is the remainder when your number is divided by 3 ?"))
            if remainder_3 < 0:
                print("The value entered must be 0 or greater")
            elif remainder_3 > 2:
                print("The value entered must be less than 3")
            else:
                print()
                break
        
        remainder_5 = 0
        remainder_5 = True

        while remainder_5:
            remainder_5 = int(input("What is the remainder when your number is divided by 5 ?"))
            if remainder_5 < 0:
                print("The value entered must be 0 or greater")
            elif remainder_5 > 4:
                print("The value entered must be less than 5")
            else:
                print()
                break
    
        remainder_7 = 0
        remaider_7 = True
    
        while remainder_7:
            remainder_7 = int(input("What is the remainder when your number is divided by 7 ?"))
            if remainder_7 < 0:
                print("The value entered must be 0 or greater")
            elif remainder_7 > 6:
                print("The value entered must be less than 7")
            else:
                print()
            break

        if((i % 3 == remainder_3) and (i % 5== remainder_5) and (i % 7 == remainder_7)):
            user_num = i

            user = input("Do you want to play again? Y to continue, N to quit ==>")
    
        if (play == "N"):
            play == False
            break

    print(f"Your number was {user_num}")
    print("How amazing was that?")
    print()
    print("Do you want to play again")

    
        
        

    


    
    
