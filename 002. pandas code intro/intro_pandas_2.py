###############################################
#  from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb
###############################################
from pandas import DataFrame,read_csv
import pandas as pd
import os
import sys
import matplotlib
import matplotlib.pyplot as plt

# print('Python version:' + sys.version)
# print('Pandas version:' + pd.__version__)
# print('Matplotlib version:' + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

#use the zip and list function to create list of tuples of (names,births)
BabyDataSet = list(zip(names,births))
#print(BabyDataSet)
df1 = DataFrame(data = BabyDataSet, columns=['Names','Birth'])
#print(df1)

### use to_csv built-in function to change dataframe into csv file
### AND save targeted csv file into designated folder location
df1.to_csv('births1880.csv',index=False,header=False)
### use read_csv to read existed csv files to dataframe

births1880_loc = r'C:\Users\garry\Documents\data-mining-for-fun\002. pandas code intro\births1880.csv'
### use read_csv to read csv files to the targeted new df2
### do not forget header=None otherwise you will get wrong column index
df2 = pd.read_csv(births1880_loc,header=None)
#print(df2)

#built-in function needs title when it has some input parameters
df2 = pd.read_csv(births1880_loc,names = ['Names','Birth'])
#print(df2)

# at the end of these actions
# if you want to remove csv file that you create
# you can use os.remove
os.remove(births1880_loc)

#print(df1)
#print(df1.dtypes)
#print(df1.Birth.dtype)


#SECTION 2 Analyzing data
df1_sorted = df1.sort_values(['Birth'],ascending=False)
# print(df1_sorted)
# print('\n')
# print(df1_sorted.head(1))
# print(df1['Birth'].max())

df1['Birth'].plot()
maxValue = df1['Birth'].max()
maxName = df1['Names'][df1['Birth'] == df1['Birth'].max()].values
print(maxName)

# combine maxValue and maxName by text
Text = str(maxValue) + '-' + maxName
print(Text)

### start to add text to graph
plt.annotate(Text,xy=(1,maxValue), xytext=(8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')
print("\nThe most popular name: ")
print(df1[df1['Birth']==df1['Birth'].max()])


