'''
Name: Jiahui Zhu
Date: 6/11/2019
'''
from numpy import *
from AprioriSimple import *

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            #print(Lk[i]);print(list(Lk[j])[:k-2])
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            #print(L1);print('----');print(L2);print('-------')
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
            #print('----',retList)
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        # print('\n'+'1111111111111111111')
        # print(L[k-2])
        # print(k)
        Ck = aprioriGen(L[k-2], k)
        #print(Ck)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        #print('-',Lk,supK)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

if __name__=='__main__':
    dataSet = loadDataSet()
    L,suppData=apriori(dataSet)
    #print(L);print('\n');print(L[0]);print('\n');print(L[1]);print('\n');print(L[2]);print('\n');print(L[3]);print('\n')
    print(aprioriGen(L[0],2))
    # print('--------------------')
    L1,suppData=apriori(dataSet,minSupport=0.7)
    #print('--/////////',L1)



