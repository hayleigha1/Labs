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
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.Keeps asking until they respond yes '''

    user_input = input("Do you want to play again? ==> ")

    
    else:
        
        while user_input.lower() not in ["yes","y","no","n"]:#while user_input.lower != "y' or 'n' or 'yes' or 'y': 

            print("You must enter Y/YES/N/NO to continue. Please try again")
            user_input = input("Do you want to play again? ==> ")
        
        if (user_input == "Y") or (user_input == "y") or (user_input == "YES") or (user_input == "yes"):

            return True

        elif (user_input == "N") or (user_input == "n") or (user_input == "NO") or (user_input == "no"):

            return False 

     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    user_wager = int(input("How many chips do you want to wager?"))

    if (user_wager >= 0) and (user_wager <= bank):

        return user_wager

    else:
        
        while (user_wager < 0) or (user_wager > bank):

            user_wager = int(input("How many chips do you want to wager?"))
            print("You must enter a valid value.")
            
        if (user_wager >= 0) and (user_wager <= bank):
            return user_wager
              

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''

    return random.randint(1,10), random.randint(1,10), random.randint(1,10)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
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
