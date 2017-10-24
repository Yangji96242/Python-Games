# < Mini Game : version 1 >
# ------------------------------------------

#     The Adventure of Jimmy & Jeff

#                        13th.Oct. 2017
# ------------------------------------------

import random


#Definitions
#Pick the character
def PickTheCharacter():
    Division()
    Player = input("Please enter one character\'s Name to continue:")
    Division()
    if Player.capitalize() == "Jimmy":
        print("Hi, I'm Jimmy \nHP : 500 \nMP : 180 \nAttack Damage :120 \nAbility Power :50")
    elif Player.capitalize() == "Jeff":
        print("Hi, I'm Jeff \nHP : 480 \nMP : 250 \nAttack Damage :60 \nAbility Power :110")
    else:
        print("You chose {}.\nHi, I\'m {}, the {}. \nHere is my profile: \nHP : {} \nMP : {} \nAttack Damage : {} \nAbility Power : {}".format(Player,Player,occupation(),random.randint(200,500),random.randint(50,150),random.randint(20,50),random.randint(10,50)))   

def RePick():
    SelectAnswer=input("Do you satisify with me?\nPress Y to start the adventure / Press N to change the character:")
    if SelectAnswer.upper() == "Y":
        print(">>>>>>>>>>>Mission 1 START<<<<<<<<<<<")
    elif SelectAnswer.upper() not in ["Y","N"]:
        print("You entered the wrong option, try again.")
        PickTheCharacter()
        RePick()
    else:    
        PickTheCharacter()
        RePick()

#occupation
def occupation():
    occu=["driver","singer","cooker","farmer","fisher","DJ"]
    from random import choice
    return choice(occu)

#Division line
def Division():
    print("------------------------------------------------------------------------")



#Content begin
#Welcome
print("Welcome to the Adventure World...")
print("Now, Let\'s begin our journey...")
input("Press Enter to continue...")
Division()

#Select a player
print("<Introduction>")
print("Character 1: Jimmy (Warrior)      - Outstanding Attack Damage")
print("Character 2: Jeff (Magician)      - Outstanding Ability Power")
print("Character 3: Other Names you like - they get different skills :)")


PickTheCharacter()
RePick()
Division()

