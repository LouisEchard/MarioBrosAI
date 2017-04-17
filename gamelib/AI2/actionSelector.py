import pygame

from enum import Enum
from bokeh.util.session_id import random
from pygame.constants import K_LEFT, K_RIGHT, K_z

class validDecisions(Enum):

    DO_NOTHING = 0

    LEFT = 1

    RIGHT = 2
    
    JUMP = 3
    
    LEFT_JUMP = 4
    
    RIGHT_JUMP = 5


TOTAL_ACTIONS = 6
actionNumber = int()

def __init__(self, actionNumber, *keys):
    self.actionNumber = actionNumber
    self.action = [None]*6
    for key in keys:
        self.action[key] = True

def getActionNumber(self):
    return self.actionNumber

def getAction(self):
    return self.action
    
def MarioAction(anEnum, aKey):
    if(anEnum==validDecisions.DO_NOTHING):
        return aKey
    elif anEnum==validDecisions.JUMP :
        aKey[K_z]=True
    elif(anEnum==validDecisions.LEFT):
        aKey[K_LEFT]=True
    elif(anEnum==validDecisions.RIGHT):
        aKey[K_RIGHT]=True
    elif(anEnum==validDecisions.LEFT_JUMP):
        aKey[K_z]=True
        aKey[K_LEFT]=True
    elif(anEnum==validDecisions.RIGHT_JUMP):
        aKey[K_z]=True
        aKey[K_RIGHT]=True
        
    return aKey
#     @classmethod
#     @getAction.register(object, int)
def getAction_0(aGame, aRandom=False):
    
    
    myKey = [False]*1000
    
    myListOfBaddies = []
    myListOfCoins = []
    myPlayerRect = aGame.player.rect
    
    for b in aGame.baddies:  
        if b.rect.colliderect(aGame.camera.rect):  
            myListOfBaddies.append(b.rect)
    
    for c in aGame.coins:
        if aGame.player.rect.colliderect(c.rect):
            myListOfCoins.append(c.rect)
    
    
    if aRandom:
        myEnum = random.choice(list(validDecisions))#[TOTAL_ACTIONS*random.random]
    else :
        theBest=validDecisions.DO_NOTHING
        theBestValue=-1000
        for context in aGame.theDecisionMaker:
            if(context[0]==myListOfBaddies and context[1]==myListOfCoins):
                if(aGame.theDecisionMaker.get(context)>theBestValue):
                    theBest=context[2]
                    theBestValue=aGame.theDecisionMaker.get(context)
                
        
        myEnum = list(validDecisions)[actionNumber]
        
    saveDecision([myListOfBaddies, myListOfCoins, myEnum], aGame)
    
    
    return MarioAction(myEnum,myKey)




def saveDecision(anEnum, aGame):
    aGame.theCumActions.append(anEnum)
    


def getDecision(randomly=False):
    Nothing =0