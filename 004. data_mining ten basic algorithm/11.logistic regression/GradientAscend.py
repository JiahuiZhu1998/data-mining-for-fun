'''
Name:Jiahui Zhu
Date: 6/10/2019
this script shows how to do gradient ascend in python
'''

from numpy import *

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('file from book/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    if inX.all()>=0:
        return 1.0 /(1 + exp(-inX))
    else:
        return exp(inX)/(1+exp(inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
    labelMat = mat(classLabels).transpose() #convert to NumPy matrix
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    #print(dataMatrix)
    for k in range(maxCycles):              #heavy on matrix operations
        h = sigmoid(dataMatrix*weights)     #matrix mult
        error = (labelMat - h)              #vector subtraction
        weights = weights + alpha * dataMatrix.transpose()* error #matrix mult
    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)#将画布分割成1行1列，图像画在从左到右从上到下的第1块
    ### s=30 s is size
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')#square marker
    ax.scatter(xcord2, ycord2, s=30, c='green')# default to be point
    x = arange(-3.0, 3.0, 0.1)#0.1地等分-3到3
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        # print(weights)
        # print(dataMatrix[i])
        # print(h)
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)  # initialize to all ones
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.0001  # apha decreases with iteration, does not
            randIndex = int(random.uniform(0, len(dataIndex)))  # go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

if __name__ == "__main__":
    dataArr,labelMat=loadDataSet()
    #part1
    #weights = gradAscent(dataArr,labelMat)
    # plotBestFit(weights.getA())
    #part2
    # weights2 = stocGradAscent0(array(dataArr),labelMat)
    # plotBestFit(weights2)
    #part3
    weights3 = stocGradAscent1(array(dataArr),labelMat,500)
    plotBestFit(weights3)


