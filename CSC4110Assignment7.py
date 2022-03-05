#revision number: 1
#begin 2/28/2022

#Issue 1
#program will:
#               Write a function, makeDictionary, that “inputs” the lists into your current program, 
#               then takes the two lists and returns a dictionary with the names as the keys and the scores as the values. 
#               Assign the result to scoreDict, which will be used in the exercises that follow

#lists 
names = ['joe' , 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]

#directory function
#input: 
#       names: list of names to be added into a dictionary 
#       scores: list of scroes to be added into a dictionary 
#output:
#       returns a dictionary
def makeDictionary(names,scores):
    dict = {}
    for name in range(len(names)):
        dict[names[name]] = scores[name]
    return dict

#create score dictioinary
scoreDict = makeDictionary(names,scores)
print(scoreDict)


#Issue 2
#program will:
#               Using scoreDict, find the score for 'barb'. It should be inside a data structure 
#               that perpetually asks for names for whom to search the score.

#print barbs score
print(scoreDict.get('barb'))


#Issue 3
#program will:
#               Add something in the function that allows you to PERPETUALLY add key/ value pairs, 
#               such as adding the name “John,” with a score of 19.

#funtion to add to dictionary 
#input: 
#       dict: dictionary if names and scores
#       name: new name to be added
#       score: new scroe to be added
#output:
#       updated dictionary
def addToDict(dict,name,score):
    dict[name] = score
    return dict
print (addToDict(scoreDict,"John",19))
scoreDict = addToDict(scoreDict,"John",19)


#Issue 4
#program will:
#               Create a sorted list of all scores in scoreDict.

sortedScores = []
sortedScoreDict = {}
#sort dictionary
sortedKeys = sorted(scoreDict, key=scoreDict.get)
for i in sortedKeys:
    sortedScoreDict[i] = scoreDict[i]
#add sorted values to a list
sortedScores = sortedScoreDict.values()
print(sortedScores)

#Issue 5
#program will:
#               Use scoreDict and create a function that perpetually gives the user the chance to do the following:
#               Add,
#               delete, 
#               query, 
#               and print all students and scores. 
#               Also, if a query results in a student search of whom doesn’t exist, 
#               then the results indicates that the student doesn’t exist

def userChoice():
    print("""Menu:\n\t0 = add\n\t1 = delete\n\t2 = query\n\t3 = print all""")
    choice = input("please enter your choice: ")
    if choice == '0':
        name = input("Enter students name: ")
        score = input("Enter students score: ")
        addToDict(scoreDict, name, score)
        print(scoreDict)
    elif choice == '1':
        scoreDict.clear()
        print(scoreDict)
        print("dictionary has been cleared")
    elif choice == '2':
        query = input("Enter the name of the student you would like to quary: ")
        if query not in sortedKeys:
            print("Student does not exist")
        else:
            studScore = scoreDict.get(query)
            print(f"{query} has a score of {studScore}")
    elif choice == '3':
        print(scoreDict)
    else:
        print("invalid option")



userChoice()
#Revision number: 2
#end 3/4/2022
# Group / manager/ lead tech/ project 
# Zion Worship Cult/ Ram Vuduku/ Rich Eissen/ the Zion Project
