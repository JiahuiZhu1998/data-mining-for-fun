####################################################################################################################
#  Python version3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
#  Pandas version0.24.2
#  Matplotlib version3.0.3
#  Name: Jiahui Zhu
#  some questions need to comprehensive below:
#  from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/04%20-%20Lesson.ipynb
#  from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/05%20-%20Lesson.ipynb
#  from https://blog.csdn.net/starter_____/article/details/79183733
#  from https://blog.csdn.net/xueruixuan/article/details/81451690
#  from https://blog.csdn.net/AnneQiQi/article/details/71057069
#  from http://www.30daydo.com/article/257
#
#  get to know what .stack and .unstack mean in dataframe
#####################################################################################################################
import pandas as pd
import sys
print('Python version:'+sys.version)
print('Pandas version:'+pd.__version__)

# how to use extend
list1 = [1,2]
list2 = [3,4]
list3 = [];list4=[]
list3.append(list1)
list3.append(list2)
list4.extend(list1)
list4.extend(list2)
print(list3)
print(list4)

# start lesson  pandas tutorial here
d1 = [0,1,2,3,4,5,6,7,8,9]
df1 = pd.DataFrame(d1)
print(df1)
## assign name to the first column of d1
df1.columns = ['Rev']
print(df1)
## add a new column to df1
df1['NewCol'] = 5
print(df1)
print('\n')
## modify new column
df1['NewCol'] = df1['NewCol']+1
print(df1)
print('\n')
## then we can delete columns
del df1['NewCol']
print(df1)
print('\n')
## lets add a couple of columns
df1['test'] = 3
df1['col'] = df1['Rev']
print(df1)
print('\n')
##if we wanted, we could change the name of the index
i =['a','b','c','d','e','f','g','h','i','j']
df1.index = i
print(df1)
print('\n')
print(df1.loc['a'])
print('\n')
print(df1.loc['a':'d'])
print('\n')
print(df1.iloc[0:3])## iloc and loc have been included in previous python script
print('\n')
print(df1['Rev'])
print('\n')
print(df1[['Rev','test']])## need to remember use  two bruckets
print('\n')
print(df1.index[0:3])
print(df1.loc[df1.index[0:3],'Rev'])
print('\n')
print(df1.loc[df1.index[5:],'col'])
print('\n')
print(df1.loc[df1.index[:3],['col','test']])
print('\n')
print(df1.head())
print('\n')
print(df1.tail())
print('\n')
#### lesson 5 starts over here
d2 = {'one':[1,1],'two':[2,2]}
i2 = ['a','b']## which means index
##create dataframe
df10 = pd.DataFrame(data=d2,index = i2)
print(df10)
print('\n')
print(df10.index)
print('\n')
stack1 = df10.stack()
print(stack1)
print('\n')
print(stack1.index)
print('\n')
unstack1 =df10.unstack()
print(unstack1)
print('\n')
print(unstack1.index)
print('\n')
print(df10.T) ### which means transpose