#revision number: 1
#begin 2/21/2022

#Issue 1
#program will:
#               1.	Print a string that uses double quotation marks inside the string.
#               2.	Print a string that uses an apostrophe inside the string.
#               3.	Print a string that spans multiple lines with whitespace preserved.
#               4.	Print a string that is coded on multiple lines but gets printed on a
#                   single line.

#1.
print(""""The greatest glory in living lies not in never falling, but in rising every time we fall." -Nelson Mandela\n """)

#2.
print("they'll be back \n")

#3
print("""And then the day came,

when the risk 
to remain tight
in a bud
war more painful
than the risk
it took 
to blossom
    -Ezra Pound\n""")

#4
str1 = "once upon a time "
str2 = "in a land far away\n"
print(str1 + str2)


#Issue 2
#program will:
#               1.	Create a string and print its length using len().
#               2.	Create two strings, concatenate them, and print the resulting string.
#               3.	Create two strings, use concatenation to add a space between them, and print the result.
#               4.	Print the string "zing" by using slice notation to specify the correct
#                   range of characters in the string "bazinga".

#1.
length = "very long"
print(len(length))

#2.
string1 = "Bob "
string2 = "Cat"
combo = string1 + string2
print(combo)

#3.
string3 = "Tom"
string4 = "Cat"
space = string3 + " " + string4
print(space)

#4.
zing = "bazinga"
print(zing[2:6])


#Issue 3
#program will:
#               1. Write a program that converts the following strings to lowercase:
#                  "Animals", "Badger", "Honey Bee", "Honey Badger". Print each lower-
#                  case string on a separate line.
#               2. Repeat exercise 1, but convert each string to uppercase instead of
#                  lowercase.
#               3. Write a program that removes whitespace from the following
#                  strings, then print out the strings with the whitespace removed:
#                  string1 = " Filet Mignon"
#                  string2 = "Brisket "
#                  string3 = " Cheeseburger "
#               4. Write a program that prints out the result of .startswith("be") on
#                  each of the following strings:
#                  string1 = "Becomes"
#                  string2 = "becomes"
#                  string3 = "BEAR"
#                  string4 = " bEautiful"

#1.
lowerCase = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
for i in range(len(lowerCase)):
    print(lowerCase[i].lower())

#2.
for j in range(len(lowerCase)):
    print(lowerCase[j].upper())


#3.
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.strip() + string2.strip() + string3.strip())

#4.
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print("string1: {}, string2: {}, string3: {}, string4: {}".format(string1.startswith("be"),
      string2.startswith("be"),string3.startswith("be"),string1.startswith("be")))


#Issue 4
#program will:
#               1. Create a string containing an integer, then convert that string into an actual integer object using int(). 
#                  Test that your new object is a number by multiplying it by another number and displaying the result.
#               2. Repeat the previous exercise, but use a floating-point number and float().
#               3. Create a string object and an integer object, then display them side by side with a single print statement using str().
#               4. Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, and displays the result.
#                  If the user enters 2 and 4, then your program should print the following text:
#                  The product of 2 and 4 is 8.0.
#               5. Use the .find()string method.

#1.
stringNum = "6"
#convert
num = int(stringNum)
print(num * 6)

#2.
stringNum = "6.6"
#convert
print(float(stringNum) * 6.6)

#3.
stringNum = "6"
num = 6
print(stringNum + str(num))

#4.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
product = num1 * num2
print("The product of {} and {} is {}.".format(num1,num2,product))

#5.
message = "I failed my way to success"
print(message.find('way'))


#Revision number: 2
#end 2/25/2022
# Group / manager/ lead tech/ project 
# Zion Worship Cult/ Ram Vuduku/ Rich Eissen/ the Zion Project