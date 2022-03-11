#revision number: 1
#begin 3/10/2022

#Issue 1
#program will:
#               1.	This app must have (at least) FOUR BUTTONS
#                   a.	One for a Madlibs game
#                   b.	Another to draw a random polygon (random sides, and color)
#                   c.	Another to draw a polygon based on user selected number of sides, length and color
#               2.	Must have a QUIT BUTTON
#               3.	Regarding the Madlib game:
#                   -	It must make use of a Dictionary (see below example).
#                   -	It must use string formatting (see below example).
#                   -	It must filter out integers, float values, and other characters, such as ‘$%^&.’

from tkinter import *
import os
import turtle
import random

#create display window 
window = Tk()
window.geometry('500x500')
window.title('Mad Gen')
Label(window, text = 'Menu',font = 'Heletica 20 bold').pack()
Label(window, text = 'Click Any One :',font = 'arial 15 bold').place(x=40,y=80)

#madlib one
def madLib():
    adjective1 = input('enter an adjective: ')
    adjective2 = input('enter an adjective: ')
    bird = input('enter a type of bird: ')
    room = input('enter a room in a house: ')
    pastVerb = input('enter a verb(past tense): ')
    verb = input('enter a verb: ')
    relName = input("enter a relitives name: ")
    noun = input('enter a noun: ')
    liquid = input('enter a liquid: ')
    verbIng = input('enter a verb ending in -ing: ')
    bodyPart = input('enter a part of the body: ')
    plrNoun = input('enter a plural noun: ')
    verbIng2 = input('enter a verb ending in -ing: ')
    noun2 = input('enter a noun: ')
    #create dictionary
    oldDict = {
        "adjective1":adjective1,
        "adjective2":adjective2,
        "bird":bird,
        "room":room,
        "pastVerb":pastVerb,
        "verb":verb,
        "relName":relName,
        "noun":noun,
        "liquid":liquid,
        "verbIng":verbIng,
        "bodyPart":bodyPart,
        "plrNoun":plrNoun,
        "verbIng2":verbIng2,
        "noun2":noun2
        }
    #check if all strings contain only A-Z
    newDict = dict()
    for (key,value) in oldDict.items():
        if oldDict.get(key).isalpha():
            newDict[key] = value
        else:
            print("Nonalphabetic character detected")
            exit

    print("it was a %s, cold November day. I woke up to the %s smell of %s roasting in the %s downstairs.I %s down the stairs to see if I could help %s the dinner. My mom said, 'See if %s needs a fresh %s.' So I carried a tray og glasses full of %s into the %s room. When I got there, I couldn't believe my %s! There were %s %s on the %s!"
          %(newDict['adjective1'],newDict['adjective2'],newDict['bird'],newDict['room'],newDict['pastVerb'],newDict['verb'],newDict['relName'],newDict['noun'],newDict['liquid'],newDict['verbIng'],newDict['bodyPart'],newDict['plrNoun'],newDict['verbIng2'],newDict['noun2']))

#exit program
def exit():
    os._exit(0)

#random polygon
def randPoly():

    #lists for random choices
    colors = ["red","green","blue","cyan","yellow","orange","purple","pink"]
    shape = ["triangle","square","pentagon","hexagon","septagon","octagon","nonagon","decagon","undecagon","dodecagon"]
    
    size = 50
    clr = random.choice(colors)
    sides = random.randint(3,12)
    angle = 360/sides

    #list for printing name
    name = shape[sides-3]

    #draw polygon function
    def drawPoly():
        t=turtle.Turtle()
        t.color(clr)
        t.begin_fill()
        for i in range(sides):
            t.forward(size)
            t.left(angle)
        t.end_fill()
        t.hideturtle()
    #polygon name(for the number of sides)
    def polyName():
        t=turtle.Turtle()
        t.penup()
        t.goto(-37, -37)
        t.write(name,font = ("Helvetica", 24))
        t.hideturtle()

    drawPoly()
    polyName()

#user choise pollygon
def polygon():

    #obtain users choices
    size = int(input('Enter the size of shape: '))
    clr = input('Enter color of shape: ')
    sides = int(input('Enter number of sides(3-12): '))
    shape = ["triangle","square","pentagon","hexagon","septagon","octagon","nonagon","decagon","undecagon","dodecagon"]
    name = shape[sides-3]
    angle = 360/sides

        #draw polygon function
    def drawPoly():
        t=turtle.Turtle()
        t.color(clr)
        t.begin_fill()
        for i in range(sides):
            t.forward(size)
            t.left(angle)
        t.end_fill()
        t.hideturtle()
    #polygon name(for the number of sides)
    def polyName():
        t=turtle.Turtle()
        t.penup()
        t.goto(-37, -37)
        t.write(name,font = ("Helvetica", 24))
        t.hideturtle()

    drawPoly()
    polyName()
    


#Create Buttons
Button(window, text = 'Madlibs game', font = 'arial 15' , command=madLib, bg = 'ghost white').place(x=150,y=150)
Button(window, text = 'Random Polygon', font = 'arial 15' , command=randPoly, bg = 'ghost white').place(x=150,y=200)
Button(window, text = 'Polygon', font = 'arial 15' , command=polygon, bg = 'ghost white').place(x=150,y=250)
Button(window, text = 'Quit', font = 'Helvetica 13 bold' , command=exit, foreground="Green",background="Yellow").place(x=150,y=300)



window.mainloop()
#Revision number: 1
#end 3/10/2022
# Group / manager/ lead tech/ project 
# Zion Worship Cult/ Ram Vuduku/ Rich Eissen/ the Zion Project