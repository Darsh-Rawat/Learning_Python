import random

'''
Logic : 

Snake[0]  vs Water[1]  > Snake W[0] 
Water[1]  vs Gun[-1]  > Water W[1] 
Gun[-1] vs Snake[0]  > Gun W [-1] 

------------------------------

Snake = 0
Water = 1
Gun = -1

'''

# Issues : 1. Can't find fix for print Name. Terminal prints 0 or 1 or -1 instead of g, s or w for bot's choice !

Options = {
    "s":0, 
    "w":1, 
    "g":-1
}

# User Input and Programed Input
Computer = random.choice(list(Options.values()))
UserInput = input("Enter Snake(s)/Water(w)/Gun(g) : ")


# Convert the input in selection from Dict : 
TextToNum = Options[UserInput]

# Conditionals :

# Bot Chooese -1 [Gun] : Below is the logic for, if the programed bot chooses Gun <>

if(Computer==-1 and TextToNum==0):
     print(f" Bot Choose {Computer} and you choose {UserInput} : You Loose")

elif((Computer==-1) and (TextToNum==1)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : You win")

elif((Computer==-1) and (TextToNum==-1)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : Hence Draw")


# Bot Chooses 1 [Water] : Below is the logic for, if the programed bot chooses Water <>

elif((Computer==1) and (TextToNum==0)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : You win")

elif((Computer==1) and (TextToNum==1)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : Hence Draw")

elif((Computer==1) and (TextToNum==-1)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : You Loose")

# Bot Chooses [Snake] : Below is the logic for, if the programed bot chooses Snake <>

elif((Computer==0) and (TextToNum==0)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : Hence Draw")

elif((Computer==0) and (TextToNum==1)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : You win")

elif((Computer==0) and (TextToNum==-1)):
    print(f" Bot Choose {Computer} and you choose {UserInput} : You Loose")



