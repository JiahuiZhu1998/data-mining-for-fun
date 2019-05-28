#################################################################################
#  Name: Jiahui Zhu
#  Date: 5/23/2019
#  Description: this is basic algorithm called k-Nearest Neighbor Algorithm
#
#################################################################################
from numpy import *
import operator


def classify0(intX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    #### distance from every point to the origin
    diffMat = tile(intX,(dataSetSize,1)) - dataSet  ### use intX which is an array to create a new array which size is (dataSetSize,1)
    #print(tile(intX,(dataSetSize,1)))
    # print('\n')
    # print(dataSet)
    # print('\n')
    # print(diffMat)
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)### add each together
    distances = sqDistances ** 0.5### make squareroot
    sortedDistIndicies = distances.argsort()
    # print('\n')
    # print(distances)
    # print(sortedDistIndicies)
    classCount = {}
    print('\n')
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] ## find the label of corresponding spot(x,y) ## fillin dictionary
        print(i)
        print(voteIlabel)
        print('/')
        ##start to use dictionary over here
        print(classCount.get(voteIlabel, 0))
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print(classCount[voteIlabel])
        print(classCount)
        sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        return sortedClassCount[0][0]
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
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
        print("the classifier came back with: %d, the real answer is: %d"%(classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))


if __name__ == '__main__':
    group1 = array([[1.,1.1],[1.,1.],[0.,0.],[0.,0.1]])
    labels1 = ['A','A','B','B']
    classify0([0,0],group1,labels1,3)
    ######################
    #pass;
