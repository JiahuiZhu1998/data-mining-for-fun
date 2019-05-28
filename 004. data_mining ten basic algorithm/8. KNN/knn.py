#################################################################################
#  Name: Jiahui Zhu
#  Date: 5/23/2019
#  Description: this is basic algorithm called k-Nearest Neighbor Algorithm
#
#################################################################################
from numpy import *
import operator
import os
from os import listdir
import sys


def classify0(intX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    #### distance from every point to the origin
    diffMat = tile(intX,(dataSetSize,1)) - dataSet  ### use intX which is an array to create a new array which size is (dataSetSize,1)
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)### add each together
    distances = sqDistances ** 0.5### make squareroot
    sortedDistIndicies = distances.argsort()
    classCount = {}##create dictionary here
    print('\n')
    for i in range(k):## this for loop pick the label which appear most frequently
        voteIlabel = labels[sortedDistIndicies[i]] ## find the label of corresponding spot(x,y) ## fillin dictionary
        #print(classCount.get(voteIlabel, 0))
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        #print(classCount[voteIlabel])
        #print(classCount)
    print(classCount.items())
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    ## this function change text to numpy array
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = [] ## create an array
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index+=1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals -minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet / tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %s, the real answer is: %s"%(classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("You will probably like this person:",resultList[classifierResult-1])
'''
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))
'''
if __name__ == '__main__':
    group1 = array([[1.,1.1],[1.,1.],[0.,0.],[0.,0.1]])
    labels1 = ['A','A','B','B']
    classify0([0,0],group1,labels1,3)
    ######################
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    ###################### use matplotlib below
    # import matplotlib
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # #ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    # ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    # plt.show()
    ######################
    normMat,ranges,minVals = autoNorm(datingDataMat)
    ######################
    datingClassTest()
    #classifyPerson()


