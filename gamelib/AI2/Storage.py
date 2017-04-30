
filePath = "/home/ldrahce/git/MarioBros-AI/gamelib/AI2/QStatesAndValues.txt"

from actionSelector import validDecisions as VD
from pygame.rect import Rect
import pygame

class HashableRect(pygame.Rect):
    def __hash__(self):
        return hash(tuple(self))

def save(dict):
    file = open(filePath, 'w')

    for obj in dict.keys():
        save = True
        myString = ""
        file.write('\n')
        for key in obj:
            if(key==()):
                myString = myString+"empty;"
            elif(key==""):
                myString=myString
            else:
                if not isinstance(key[0], int):
                    myRect = key[0]
                else:
                    myRect = key
                myString=myString+str(myRect.left)+":"+str(myRect.top)+":"+str(myRect.width)+":"+str(myRect.height)+";"

        if save and obj!=():
            file.write(myString+" ,Results ")
            for enum in VD:
                if len(dict[obj])<5:
                    stop=True
                file.write(str(dict[obj][enum.value])+':')


def load(dict):
    def __hash__(self):
        return hash(tuple(self))
    myLastTuple=()
    first=True
    myArrayOfResults=[]
    with open(filePath) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            if(line!=""):
                myResults=line.split(" ,Results ")
                mySplitResults=myResults[1].split(":")
                myContexts=myResults[0].split(";")

                myTuple=()

                for stri in myContexts:
                    if(stri=="empty"):
                        myTuple = myTuple + ((),)
                    elif(stri!=""):
                        myDim=stri.split(":")
                        myRect = Rect(int(myDim[0]),int(myDim[1]),int(myDim[2]),int(myDim[3]))
                        myTuple = myTuple + ((HashableRect(myRect)),)

                if(myTuple!=myLastTuple):
                    dict[(myLastTuple)] = myArrayOfResults
                    myArrayOfResults=[]
                myArrayOfResults=mySplitResults

                myLastTuple=myTuple
    return dict


