#####################################################
# NAME: Jiahui Zhu                                  #
# Email: zhuzhuxia555555@gmail.com                  #
# problem description: using decision tree and      #
#   random decision forests to                      #
# predict the winner of NBA champion                #
#####################################################

import pandas as pd
import numpy as np
import sys
import os
import math
from collections import defaultdict
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

dataset = pd.read_csv('C:/Users/garry/Documents/data-mining-for-fun/Project  NBA Winner Prediction/basketball.csv',parse_dates=["Date"])
dataset.columns = ["Date", "Start (ET)", "Visitor Team", "VisitorPts", "Home Team", "HomePts", "OT?", "Score Type", "Attend.", "Notes"]
dataset["HomeWin"] = dataset["VisitorPts"] < dataset["HomePts"]
#print(dataset)
y_true = dataset["HomeWin"].values
meanHomeWIN = dataset["HomeWin"].mean()

## start to compare these teams
won_last = defaultdict(int)
#print(won_last)
dataset['HomeLastWin'] = 0
dataset['VisitorLastWin'] = 0
## HomeLastWin & VisitorLastWin are two boolean values that show visitor or home win or not in last game
for index, row in dataset.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']
    #print(row)
    row['HomeLastWin'] = won_last[home_team]
    dataset.set_value(index,'HomeLastWin',won_last[home_team])
    dataset.set_value(index,'VisitorLastWin',won_last[visitor_team])
    won_last[home_team] = int(row['HomeWin'])
    won_last[visitor_team] = 1- int(row['HomeWin'])
    # print(won_last[home_team])
    # print(won_last[visitor_team])
    # print('\n')

### we set min_samples_split and min_samples_leaf to pruning the decision tree
### the way to create decision tree is use Gini impurity and information gain
    clf = DecisionTreeClassifier(random_State=14)
    X_previouswins = dataset[['HomeLastWin', 'VisitorLastWin']].value
    scores = cross_val_score(clf, X_previouswins, y_true, scoring='accuracy')
    print('Accuracy:{9:.1f}%'.format(np.mean(scores)*100))





