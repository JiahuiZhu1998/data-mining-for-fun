####################################################################################################################
#
# Name: Jiahui Zhu
#
# Version: Python version 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
#                 Pandas version 0.24.2
# from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/06%20-%20Lesson.ipynb
# from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/07%20-%20Lesson.ipynb
####################################################################################################################
import pandas as pd
import sys

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

d1 = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}
df1 = pd.DataFrame(d1)
one1 = df1.groupby('letter')
print(one1.sum())
print('\n')
letterone1 = df1.groupby(['letter','one']).sum()
print(letterone1)
print(letterone1.index)
print('\n')
letterone2 = df1.groupby(['letter','one'],as_index=False).sum()
print(letterone2)
print(letterone2.index)
print('\n')
########################################################################################################
States2 = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']
data2 = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index2 = pd.date_range(start='1/1/2012',periods=10,freq='MS')
df2 =pd.DataFrame(data2,index2,columns=['Revenue'])
df2['State'] = States2
#print(df2)
data3 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
index3 = pd.date_range(start='1/1/2013',periods=10,freq='MS')
df3 = pd.DataFrame(data3,index3,columns=['Revenue'])
df3['State'] = States2
#print(df3)
df4 = pd.concat([df2,df3])
#print(df4)

###### Ways to calculate outliers
# method 1
newdf1 = df4.copy()
#print(newdf1)
newdf1['X-Mean'] = abs(newdf1['Revenue']-newdf1['Revenue'].mean())
newdf1['1.96*std'] = 1.96*newdf1['Revenue'].std()
newdf1['Outlier'] = newdf1['X-Mean']>newdf1['1.96*std']
#print(newdf1)

# method 2 groupby items
newdf2 = df4.copy()
## get confused about three lines below
# newdf2['Outlier'] = newdf2.groupby('State').transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
# newdf2['X-Mean']=newdf2.groupby('State').transform(lambda x:abs(x-x.mean()))
# newdf2['1.96*std']=newdf2.groupby('State').transform(lambda x:1.96*x.std())
# print(newdf2)

# 2.1
newdf3 = df4.copy()

State3 = newdf3.groupby('State')

def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96*group['Revenue'].std()
    group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
    return group

Newdf3 = State3.apply(s)
print(Newdf3)


# 2.2
# 2.3
# method 3
# 3.1
# 3.2








