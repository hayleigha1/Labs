########################################################################
##
## CS 101 Lab
## Program # Week 6; Lab 5
## Name: Hayleigh Arnold
## Email: hca8qp@umsystem.edu
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


# import statements
import string

# functions
def character_value(char):
    value = ord(char)
    value = value - 65
    return value

def get_school(string): 
    if string[5] == "1":
        return "School of Computing and Engineering SCE"
    elif string[5] == "2":
        return "School of Law"
    elif string[5] == "3":
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

def get_grade (library_card):
    if library_card[6] == '1':
        return "Freshman"
    elif library_card[6] == '2':
        return "Sophomore"
    elif library_card[6] == '3':
        return "Junior"
    elif library_card[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"

def get_check_digit(library_card):
    sum = 0
    for i in range (len(library_card)):
        value = character_value(library_card[i])
        sum += (i + 1)*value
    total = sum
    check_digit = sum%10
    return check_digit

def verify_check_digit(library_card):
    for i in range (0,5):
        if len(library_card) != 10:
            return False, "The length of the number given must be 10"

    for i in range (0,5):
        if (ord(library_card[i]) < 65) or (ord(library_card[i]) > 90):
            error = str(library_card[i])
            i = str(i)
            return False, "The first 5 characters must be A-Z, the invalid character is at " + i + " is " + error

    for i in range(7,10):
        if (library_card[i] < '0') or (library_card[i] > '9'):
            error = str(library_card[i])
            i = str(i)
            return False, "The last 3 characters must be 0-9, the invalid character is at " + i + " is " + error
        else:
            return True, ""

    for i in range(6):
        if (library_card[5] != "1") and (library_card[5] != "2") and (library_card[5] != "3"):

            return False, "The sixth character must be 1 2 or 3"

    for i in range(7):
        if (library_card[6] != "1") or (library_card[6] != "2") or (library_card[6] != "3") or (library_card[6] != "4"):
            return False, "The seventh character must be 1 2 or 3"
    for i in range (10):
        if library_card[9] != get_check_digit(library_card):
            error = str(library_card[9])
            correct = str(get_check_digit(library_card))
            return False, "Check Digit " + error + " does not match calculated value " + correct + " ."
        else:
            return True, ""
    
    
    
    
        
    
    
    

if __name__ == "__main__":

    # main program
    print(f'{"Linda Hall":^60}')
    print(f'{"Library Card Check":^60}')
    print("==" * 30)
    
    
    
    library_card = input("Enter Library Card.  Hit Enter to Exit ==> ")
    
    
    
