'''
Name:Jiahui Zhu
Date: 6/10/2019
'''
from numpy import *
from stdLinearRegression import *
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)


def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m))) #identity matrix
    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]     #
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))#高斯核计算方式（此处多乘一次diffMat)
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr,xArr,yArr,k=1.0):  #loops over all the data points and applies lwlr to each one
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

def lwlrTestPlot(xArr,yArr,k=1.0):  #same thing as lwlrTest except it sorts X first
    yHat = zeros(shape(yArr))       #easier for plotting
    xCopy = mat(xArr)
    xCopy.sort(0)
    for i in range(shape(xArr)[0]):
        yHat[i] = lwlr(xCopy[i],xArr,yArr,k)
    return yHat,xCopy

def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()

if __name__  == '__main__':
    xArr,yArr = loadDataSet('file from book/ex0.txt')
    lwlr(xArr[0],xArr,yArr,1.0)
    lwlr(xArr[0],xArr,yArr,0.001)
    yHat = lwlrTest(xArr,xArr,yArr,0.003)
    xMat = mat(xArr)
    #print(xMat[:,1])
    srtInd = xMat[:,1].argsort(0)##按列排序
    #print(srtInd)
    xSort=xMat[srtInd][:,0,:]

    ax.scatter(xMat[:,1].flatten().A[0],mat(yArr).T.flatten().A[0],s=2,c='red')
    #plt.show()
    ###
    print('----------------------------')
    abX,abY = loadDataSet('file from book/abalone.txt')
    yHat01=lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)
    yHat1 =lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
    yHat10=lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)
    print(rssError(abY[0:99], yHat01.T))
    print(rssError(abY[0:99], yHat1.T))
    print(rssError(abY[0:99], yHat10.T))
    print('----------------------------')

    yHat01_2=lwlrTest(abX[100:199],abX[0:99],abY[0:99],0.1)
    yHat1_2 =lwlrTest(abX[100:199],abX[0:99],abY[0:99],1)
    yHat10_2=lwlrTest(abX[100:199],abX[0:99],abY[0:99],10)
    print(rssError(abY[100:199], yHat01_2.T))
    print(rssError(abY[100:199], yHat1_2.T))
    print(rssError(abY[100:199], yHat10_2.T))
    print('----------------------------')
    ws3 = standRegres(abX[0:99],abY[0:99])
    yHat3 =mat(abX[100:199])*ws3
    #print(type(array(yHat3.T)))
    print(rssError(abY[100:199],array(yHat3.T)))