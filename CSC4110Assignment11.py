#revision number: 1
#begin 3/28/2022
import math

#Issue 1
#program will:
#               Compute the area of a circle
#               input: Radius
#               output: Area of the circle
def areaOfCircle(**args):
    return args['radius'] * args['radius'] * 3.14159
print(areaOfCircle(radius = 5))

#Issue 2
#program will:
#               compute length of a cube
#               input: voulme
#               output: length of the cube
def volumeOfCude(**args):
    return args['volume'] **(1/3)
print(volumeOfCude(volume = 729))

#Issue 3
#program will:
#               comput the hypotenuse of the triangle
#               input: a and b (two shortest sides)
#               output: hypotenuse
def hypotenuse(**args):
    hypotenuse = args['a'] * args['a'] + args['b'] * args['b']
    return math.sqrt(hypotenuse)
print( hypotenuse(a = 10, b = 18))

#Issue 4
#program will:
#               comput equation
#               input: 1-9 integers
#               output: equation output
def equation(**args):
    return math.sqrt((pow(args['a']+args['b'],3) - args['c'])/ (args['d'] + (args['e']-args['f']) * pow(args['g'] - args['h'], args['i'])))
print(equation(a = 4.172, b=9.131844, c=18, d=-3.5, e=11.2, f=4.6, g=7, h=2.91683, i=-.04 ))

#Issue 4
#program will:
#              What is the output of the following pieces of code, and WHY?
#              A.	TRY to PREDICT the code WITHOUT running the code
#              B.	RUN the code and PASTE the results
#              C.	Were they what you expected? Why and/ or Why Not?
def f(a,b=4,c=5):
    print(a,b,c)

f(1,2)

def f(a,b,c=5):
    print(a,b,c)
f(1,c=3,b=2)

#Revision number: 1
#end 4/1/2022
# Group / manager/ lead tech/ project 
# HALF-LIFE/ Ron Bass/ John Richards Sr./ After-Burner Elite
