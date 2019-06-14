'''
Name:Jiahui Zhu
Date:6/15/2019
'''
import os
from tree import *
def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict
if __name__=='__main__':
    simpDat=loadSimpDat()
    print(simpDat)
    initSet=createInitSet(simpDat)
    print(initSet)
    myFPtree, myGenderTab=createTree(initSet,3)
    print(myFPtree.disp())