'''
Name: Jiahui Zhu
Date: 6/4/2019

'''
import re
from numpy import *
from bayes_JiahuiZhu import createVocabList
from bayes_JiahuiZhu import bagOfWords2VecMN
from bayes_JiahuiZhu import classifyNB
from bayes_JiahuiZhu import trainNB0
def textParse(bigString):  # input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = [];
    classList = [];
    fullText = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # create vocabulary
    trainingSet = range(50);
    testSet = []  # create test set
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat = [];
    trainClasses = []
    for docIndex in trainingSet:  # train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:  # classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print
            "classification error", docList[docIndex]
    print
    'the error rate is: ', float(errorCount) / len(testSet)
    # return vocabList,fullText


if __name__=='__main__':
    mySent='This book is the best book on Python or M.L. I have ever laid eyes upon.'
    regEx = re.compile('\\W+')
    listOfTokens = regEx.split(mySent)
    for tok in listOfTokens:
        if len(tok)>0:pass;
        else:listOfTokens.remove(tok);
    print(listOfTokens)
    for tok1 in listOfTokens:
        if len(tok1)<=0:listOfTokens.remove(tok1)
    print(str(listOfTokens).lower())
    print(str(listOfTokens).upper());print('\n')

    emailText = open('file from book/email/ham/6.txt').read()
    listOfTokens = regEx.split(emailText)