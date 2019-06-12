'''
Name:Jiahui Zhu
Date: 6/10/2019
'''
from numpy import *
import matplotlib.pyplot as plt
fig=plt.figure()

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    #print(dataMat);print(labelMat)
    return dataMat,labelMat

def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    # print(xTx)
    # print(xTx.I)
    ws = xTx.I * (xMat.T*yMat)
    #print(ws)
    return ws

if __name__=='__main__':
    xArr,yArr = loadDataSet('file from book/ex0.txt')
    ws = standRegres(xArr,yArr)
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat*ws
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy*ws
    ax.plot(xCopy[:,1],yHat)
    plt.show()
    print(corrcoef(yHat.T,yMat))