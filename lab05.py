########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    user_input = input("Do you want to play again? ==>")

    while (user_input.upper() != "YES") and (user_input.upper() != "Y") and (user_input.upper() != "NO") and (user_input.upper() != "NO"):
        print("Try again.")
        user_input = input("Do you want to play again?")
    if (user_input.upper() == "YES") or (user_input.upper() == "Y"):
        return True
    elif (user_input.upper() == "NO") or (user_input.upper() == "N"):
        return False
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input("How many chips do you want to wager? ==> "))

    while (wager < 0) or (wager > bank):
        if(wager < 0):
            print("The wager amount must be greater than 0.  Please enter again. ")
            wager = int(input("How many chips do you want to wager? ==> "))
        elif(wager > bank):
            print("The wager amount cannot be greater than how much you have. ", bank)
            wager = int(input("How many chips do you want to wager? ==> "))

    return wager

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    

    return random.randint(1,10),random.randint(1,10),random.randint(1,10)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb) and (reela == reelc):
        return 3
    elif (reela == reelc) and (reela != reelb):
        return 2
    elif (reela == reelb) and (reela != reelc):
        return 2
    elif (reelb == reelc) and (reelb != reela):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input("How many chips do you want to start with? ==> "))

    while (bank < 0) or (bank > 100):
        if (bank < 0):
            print("Too low a value, you can only choose 1 - 100 chips ")
            bank = int(input("How many chips do you want to start with? ==> "))
        elif (bank > 100):
            print("Too high a value, you can only choose 1 - 100 chips ")
            bank = int(input("How many chips do you want to start with? ==> "))
        
    return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return (wager * 10)
    elif matches == 2:
        return (wager * 3)
    else:
        return (wager * -1)

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
