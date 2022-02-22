#revision number: 1
#begin 2/13/2022
#Issue 1
#program will:
#               pertain 14 different steps
                        
#1.first name declaration (lower case)
firstname = "timothy"

#2.last name declaration (upper case)
lastname = "ARMSTRONG"

#3.change first name to upper case leter, change last name to lower case
fn = firstname.upper()
ln = lastname.lower()

#print "Hello, <first name> <last name>"
print(f'Hello, {fn} {ln}')

#4. print out two new lines
print(f'\n\n')

#5. Creates a new variable that stores your first and last name together with a space between both parts.
fullname = fn + " " + ln

#6. slice and print out the last anem form the variable created in 5
#   Note: must be done in one line  timothy Armstrong
print(fullname[8:17])

#7. Replaces your last name in the variable you created in step 5 with "<your last name>, Walsh College Student"
#cut last name
fullname = fullname[0:8]
#add "<your last name>, Walsh College Student"
fullname += "ARMSTRONG, Walsh College Student"
#print new variable
print(fullname)

#8. print the following statment:
#                                   "Start by doing what's necessary; then do 
#                                   what's possible; and suddenly you are doing 
#                                   the impossible - Francis of Assisi"
#Note: using """ to allow for all special characters to be used
print(f""""Start by doing what's necessary; then do\nwhat's possible; and suddenly you are doing\nthe imposible - Francis of Assisi" """)

#9. store 2 deciaml numbers as variables 
num1 = 1.1
num2 = 2.2

#10. Stores one addition, one subtraction, one multiplication, and one division operation of these variables as variables.
#addition
numadd = num1 + num2
#subtraction
numsub = num2 - num1
#multiplication 
nummul = num1 * num2
#divition
numdiv = num2 / num1

#11. print out each of the four results using differnent methods
#concatination
print(str(num1) + " plus " + str(num2) + " equals " + str(numadd))
#string formating
formating = "{0} minus {1} equals {2}".format(num2,num1,numsub)
print(formating)
#f-string
print(f'{num1} multiply {num2} equals {nummul:.2f}')
#string formating method call
sfmc = "{x:.2f} divide {y:.2f} equals {z:.2f}"
print(sfmc.format(x = num2, y = num1, z = numdiv))

#12.square root nummul and print out result
sq_root = nummul ** 2
print(f'The square root of {nummul:.2f} equals {sq_root:.2f}')

#13. Stores the current month as a string variable (e.g. March, June, etc.) and day of the month as a numeric variable
month = "February"
day = 15

#14. Outputs "Today is day <day of month> of the month of <month variable>."
#    Note: use a diffent method from the way used in step 12
today = "\n\t\tToday is day {0} of the month of {1}"
print(today.format(day, month))


#Revision number: 4
#end 2/16/2022
# Group / manager/ lead tech/ project 
# Omega - Cypress International Equity Division / Ram Fujitsu / Rich Alderman / grant $3700