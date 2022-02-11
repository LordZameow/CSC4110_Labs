#revision number: 1
#begin 2/04/2022
#Issue 1
#program will:
#               Please enter a string:
#               Python (user imput)
#               You entered Python and its type is <class 'str'>
#               Please enter an integer:
#               123 (user imput)
#               You entered 123 and its type is <class 'str'>

#obtain user input and print it
answer = input("Please enter a string: ")
print(f'you entered {answer} and its type is {type(answer)}\n')

#obtain user input an print it
integer = input("Please enter an integar: ")
print(f'you entered {integer} its type is {type(integer)} \n\n')


#Issue 2
#program will:
#               Twinkle, twinkle, little star,
#                   How I wonder what you are! 
#                       Up above the world so high,   		
#
#                       Like a diamond in the sky. 
#               Twinkle, twinkle, little star, 
#                   How I wonder what you are

print(f'Twinkle, twinkle, little star,')
print(f'\tHow I wonder what you are!')
print(f'\t\tUp above the world so high,\n')
print(f'\t\tLike a diamond in the sky.')
print(f'Twinkle, twinkle, little star,')
print(f'\tHow I wonder what you are')


#Issue 3
#program will:
#               r = 1.1
#               Area = 3.8013271108436504

#obtain radius
radius = input("\nEnter radius of the circle: ")
#create pi
pi = 3.141592653589793
#get area
area = pi * float(radius) ** 2
#print answer
print("Radius: ",radius)
print("Area: ",area)


#Issue 4
#program will:
#               Write a Python program to test whether an inputted letter is a vowel or not.
#               
#               Note: The output is left up to the programmer.
char = input("\nEnter only one character: ")
if char in["a","e","i","o","u","A","E","I","O","U"]:
    print(f'Character {char} is a vowel\n')
else:
    print(f'Character {char} is not a vowel\n')



#Issue 5
#program will:
#               Use “list comprehension” to produce the following output:
#               [0,1,16,81,256,625,1296,2401,4096,6561,10000,14641,20736
#               ,28561,38416,50625,65536,83521,104976]
#               Requirements: code must be one line

#requires two lines to create and print the list
powfour = [i ** 4 for i in range(19)] 
print(powfour)



#Issue 6
#program will:
#               (1)	Research Roulette wheels, and make a list of all possible slots, 
#                   within the wheel, such as “RED 23.” Include 0 and 00.
#               (2)	Let the user randomly select a slot
#               (3)	Create a list called LOG, and place each selection in the log, LEFTSIDE first.
#                   Note:all implementation details of this problem to YOU.
import random


def RouletteWheel():
    #list of all posible slots
    wheel =["Green 0", "Red 1", "Black 2", "Red 3", "Black 4", "Red 5", "Black 6", "Red 7", "Black 8", "Red 9",
            "Black 10", "Red 11", "Black 12", "Red 13", "Black 14", "Red 15", "Black 16", "Red 17", "Black 18",
            "Red 19", "Black 20", "Red 21", "Black 22", "Red 23", "Black 24", "Red 25", "Black 26", "Red 27", 
            "Black 28", "Red 29", "Black 30", "Red 31", "Black 32", "Red 33", "Black 34", "Red 35", "Black 36", 
            "Green 00"]
    LOG =[]
    print("Welcome to random Roulette!")
    
    #loop for spins
    for i in range(10):
        input("press Enter to pick a random slot")#user interaction
        #obtain random slot choice
        spin = random.choice(wheel)
        print(f'{spin} was chosen\n')
        #log spins
        LOG.append(spin)
    return LOG

#prints log
log = RouletteWheel()
print(*log, sep='\n')

   


#Issue 7
#program will:
#               Make a list of people you’d like to invite to dinner. Add them using the following design:
#               -	The user is asked to name each guest, one by one (first and last name). Make sure you use a variety of 
#                   guests names...some short (say 'Dan_Evans') and names that are longer (for example, Theresa_Mcsimmons).
#               -	Each answer is added to a list called “DinnerGuests.” 
#               -	Have a SECOND LIST, populated with the date that each guest was invited with user-entered data
#               -	Have your PC output the NAME of the guest, and the DATE they were invited, in one line.
#               -	Additionally, there is an issue with dinner guest tags. You know, those ID tags people place on their outfit....
#                   the company that made the tags made some SMALL and some BIG. So, your task is to identify each guest name by the 
#                   SIZE of ID tag. You might have a print statement that says "AL_JONES goes on a small tag."
#               -	you MUST use the following: INDEXING and SLICING
#               -	additionally, you MUST use the following string backlash characters: "\t" and "\n"
#               Note: all implementation details of this problem to YOU.

def DinnerInvitations():
    #list for guests names and date they where invited 
    DinnerGuests = []
    invitedate = []
    tagsize = []


    input("Press enter to create a guest list;\twhen finished type done and hit enter 3 times")#user interaction
    #loop for Guest names and invite dates
    while "done" not in DinnerGuests:
        guest = input(f'\nPlease enter Guests first and last name: ')
        date = input(f'Please enter the Date {guest} was invited (month/day/year): ')
        size = input(f'Please enter tag size(small or big): ')
        DinnerGuests.append(guest)
        invitedate.append(date)
        tagsize.append(size)
    DinnerGuests.pop(len(DinnerGuests)-1)

    #print guest list 
    print("-----------Guest List-----------")
    print(f'Guest Name\tinvitation date\ttag size')
    for i,y,k in zip(DinnerGuests,invitedate,tagsize):
        print(i,y,k)
    

DinnerInvitations()





    


#Revision number: 3 
#end 2/10/2022
# Group / manager/ lead tech/ project 
# Omega / Ram Valud / Michael Walker / project greenwood321 