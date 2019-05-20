#####################################################
# NAME: Jiahui Zhu                                  #
# Email: zhuzhuxia555555@gmail.com                  #
# problem description: using decision tree and      #
#   random decision forests to                      #
# predict the winner of NBA champion                #
# DATE: 5/19/2019                                   #
#####################################################
## from https://blog.csdn.net/qq_30982323/article/details/82813990
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
y_true = dataset["HomeWin"].values
meanHomeWIN = dataset["HomeWin"].mean()

## start to compare these teams
won_last = defaultdict(int)
dataset['HomeLastWin'] = 0
dataset['VisitorLastWin'] = 0
## HomeLastWin & VisitorLastWin are two boolean values that show visitor or home win or not in last game
for index, row in dataset.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']
    row['HomeLastWin'] = won_last[home_team]
    dataset.loc[index,'HomeLastWin']= won_last[home_team]
    dataset.loc[index,'VisitorLastWin']=won_last[home_team]
    won_last[home_team] = int(row['HomeWin'])
    won_last[visitor_team] = 1- int(row['HomeWin'])

### we set min_samples_split and min_samples_leaf to pruning the decision tree
### the way to create decision tree is use Gini impurity and information gain
clf = DecisionTreeClassifier()
X_previouswins = dataset[['HomeLastWin', 'VisitorLastWin']].values
scores = cross_val_score(clf, X_previouswins, y_true, scoring='accuracy',cv=3)
print("Accuracy:{:.1f}%".format(np.mean(scores)*100) )

standings = pd.read_csv('C:/Users/garry/Documents/data-mining-for-fun/Project  NBA Winner Prediction/standings.csv',delimiter=',',encoding='utf-8-sig')
dataset['HomeTEamRanksHigher'] = 0
for index,row in dataset.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']
    home_rank = standings[ standings['Team']== home_team]['Rk'].values[0]
    visitor_rank = standings[standings["Team"] == visitor_team]["Rk"].values[0]
    dataset.loc[index, "HomeTeamRanksHigher"] =int(home_rank > visitor_rank)
X_homehigher = dataset[["HomeTeamRanksHigher", "HomeLastWin", "VisitorLastWin", ]].values

clf = DecisionTreeClassifier()
scores = cross_val_score(clf, X_homehigher, y_true, scoring='accuracy',cv=3)
print("Accuracy: {0:.1f}%".format(np.mean(scores) * 100))

last_match_winner = defaultdict(int)
dataset['HomeTeamWonLast']= 0

for index,row in dataset.iterrows():
    home_team = row['Home Team']
    visitor_team = row["Visitor Team"]
    teams = tuple(sorted([home_team, visitor_team]))
    home_team_won_last = 1 if last_match_winner[teams]== row['Home Team'] else 0
    dataset.loc[index,'HomeTeamWonLast']= home_team_won_last
    winner = row['Home Team'] if row['HomeWin'] else row['Visitor Team']
    last_match_winner[teams] = winner

X_lastwinner = dataset[['HomeTeamWonLast','HomeTEamRanksHigher','HomeLastWin','VisitorLastWin']].values
clf = DecisionTreeClassifier(criterion='entropy')
scores = cross_val_score(clf,X_lastwinner,y_true,scoring='accuracy',cv=3)
print('Accuracy:{0:.1f}%'.format(np.mean(scores)*100))

###
from sklearn.preprocessing import LabelEncoder

encoding = LabelEncoder()
encoding.fit(dataset['Home Team'].values)
home_teams = encoding.transform(dataset['Home Team'].values)
visitor_teams = encoding.transform(dataset['Visitor Team'].values)
X_teams = np.vstack([home_teams,visitor_teams]).T


from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder(categories='auto')
X_teams = onehot.fit_transform(X_teams).todense()

clf=DecisionTreeClassifier()
scores = cross_val_score(clf,X_teams,y_true,scoring='accuracy',cv=3)
print('Accuracy:{0:.1f}%'.format(np.mean(scores)*100))