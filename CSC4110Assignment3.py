#revision number: 1
#begin 1/28/2022
#Issue 1
#program will:
#               prompts for a number, takes that number, adds 2, 
#               multiplies by 3, subtracts 6, and divides by 3. 
val = int(input("Enter a integer: "))
val = (((val + 2)* 3 - 6) / 3)
print(val)



#Issue 2
#program will:
#               Execuse the following code groups
#               Group one:
#               my_var1 = 7.0
#               my_var2 = 5
#               print(my_var1 % my_var2)

#               Group two:
#               x = 4
#               y = 5
#               print(x//y)

#               Group three:
#               30-3**2+8//3**2*10

print("Group One")
my_var1 = 7.0
my_var2 = 5
print(my_var1 % my_var2)

print("Group Two")
x = 4
y = 5
print(x//y)

print("Group Three")
print(30-3**2+8//3**2*10)



#Issue 3
#program will:
#               Prompt for input and then print the input as a string, 
#               an integer, and a float-point value. What values can you 
#               input and print without errors being generated?

value = input("Enter a value: ")
#casts value to int
print(int(value))
#casts value to float
print(float(value))
#casts value to string
print(str(value))



#Issue 4
#program will: 
#               are there any differences in the fallowing expressions
#               (a) 2**2**3 
#               (b) 2**(2**3) 
#               (c) (2**2)**3 

a = 2**2**3
b = 2**(2**3)
c = (2**2)**3
print("Output of expression a: ",a)
print("Output of expression b: ",b)
print("Output of expression c: ",c)

#compare outputs
if (a==b==c):
    print("No differences")
if (a==b!=c):
    print("C has a different output")
if (a==c!=b):
    print("B has a different output")
if (b==c!=a):
    print("A has a different output")
if (a!=b!=c):
    print("All values are differnet")



#Issue 5
#program will: 
#               Game of chance
#               (a) build and populate treasure chest with as many items customer requires
#               (b) create a bank / loot stash
#               (c) wagers to be placed per “spin” or treasure chest “grab”
#               (d) customer “plays” until bank account reaches 0 or below.
#random libraby required
import random

print("""
____________________¶¶¶
_____________________¶
_____________________¶¶¶¶¶¶¶¶¶¶¶¶¶
_____________________¶¶¶___¶__¶_¶¶¶¶
_____________________¶¶¶___¶¶¶¶___¶¶
_____________________¶¶¶__¶¶¶¶¶___¶¶
_____________________¶¶¶__¶¶¶¶¶___¶
_____________________¶¶¶¶¶¶__¶¶___¶
_____________________¶_________¶¶¶¶
_____________¶¶¶¶¶¶¶¶¶¶¶¶¶
_____________¶¶___________¶¶
______________¶____________¶
______________¶_____________¶
_______________¶____________¶
_______________¶____________¶_¶¶
_______________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶
_____¶____________¶¶_____________¶¶____¶
_____¶¶____________¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶
______¶¶_____¶¶___________¶______________¶¶
_______¶______¶____________¶______________¶
_______¶______¶¶___________¶_____________¶¶
_______¶_______¶___________¶_____________¶¶
______¶¶_______¶___________¶¶____________¶
______¶¶¶¶¶¶¶¶¶¶¶__________¶¶___________¶¶
___________¶_¶_¶¶________¶¶¶_____¶¶¶¶¶¶¶¶_____¶¶¶
___________¶_¶_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶_______¶¶¶¶¶__¶¶
¶¶¶¶¶¶_____¶_¶______¶¶_¶_______¶_¶¶¶¶¶¶¶¶¶___¶¶¶¶¶
¶¶___¶¶¶¶¶¶¶¶¶______¶¶_¶____¶¶¶¶¶¶¶________¶¶
__¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶______¶
____¶____________________________¶¶_¶____¶
_____¶_____¶¶¶_____¶¶_____¶¶¶_____¶¶¶___¶¶
______¶___¶¶_¶¶___¶¶_¶____¶_¶¶__________¶
______¶¶____¶¶_____¶¶¶_____¶¶__________¶¶
_______¶¶_____________________________¶¶
________¶¶___________________________¶¶
_________¶¶________________________¶¶¶
___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
""")
print("PIRATE")

#build tresure chest
input('Press build your chest;\tadd one gold;\ttype exit to finish')

#create/fill treasure chest
treasure_chest = []
while "exit" not in treasure_chest:
    booty = input("Enter objects to store in chest: \n")
    treasure_chest.append(booty)
treasure_chest.pop(len(treasure_chest)-1)
print(treasure_chest)

#fill loot stash
input('press ENTER put money in matey')
balance = float(input('Enter BEGGINNING balance: \n'))
print(balance)

#bet till balance is <=0
while balance != 0:
    input('press ENTER to place bet.')
    bet = int(input(f'Place wager: \nNote: Avilible loot: {balance}.\n'))
    print("Note: you bet:" ,bet)
    input("Arr get ready to spin the wheel!")

    #spin the wheel
    spin = random.choice(treasure_chest)
    print(f'you got: {spin}!!')

    if spin == "gold":
        print("you WIN!!")
        balance += bet
        print(f'Avilible loot: {balance}.\n')
    else:
        balance -= bet
        print(f'Avilible loot: {balance}.\n')
    




#Issue 6
#program will:
#               (a) create random passwords in perpetuity
#               (b) if the password is “acceptable,” it gets archived
#               (c) “unaccepted” passwords get deleted
#               (d) no less than 40 iterations
#random library requied 

#generate random password of 42 chars in length
def GenPassword():
    password=""
    while True:
        for i in range(42):
            info = random.randrange(60,123,1) #generate random characters
            password += chr(info)
        break
    return passwd


#check rockyou.txt for password
def CheckDictionary(passwd):
    f = open('rockyou.txt','r') #opens rockyou.txt
    for line in f: #loops to compare passwd with all rockyou.tet passwords
        if passwd == line:
            print("unaccepted")
        else:
            return passwd

#check password length and for special characters
def CheckPassword(passwd):
    #check if password is under 40 charicters
    if len(passwd) < 40:
                print ("unaccepted")
    else:            
        #check for special characters
        for i in passwd:
                if i in ["!","#","$""%","&","'","(",")","*","+",
                         ",","-",".","/",":",";","<","=",">","?",
                         "@","[","\",",",","]","^","_","`","{","|",
                         "}","~"]:
                    #returns password
                    return passwd
                else: 
                    pass



#generate and arcive 10 passwords
passwdList = []
for i in range(10):
    passwd = GenPassword()
    passwdList.append(CheckDictionary(CheckPassword(passwd))) 
    

#print arcive
print(*passwdList, sep = "\n")

                

#Revision number: 3 
#end 2/4/2022
## Group / manager/ lead tech/ project # Omega / Ram Valud / Michael Walker / project greenwood321 
                



