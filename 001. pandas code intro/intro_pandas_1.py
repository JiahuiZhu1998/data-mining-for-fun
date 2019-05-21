#############################################################################################################
#Python version3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
#Pandas version0.24.2
#Matplotlib version3.0.3
# Jiahui Zhu
# Date:5/15/2019
#
# from https://github.com/codebasics/py/tree/master/pandas/2_dataframe_basics
# from https://github.com/codebasics/py/tree/master/pandas/1_intro
# from https://blog.csdn.net/qq_30982323/article/details/82813990
# from https://data-flair.training/blogs/python-defaultdict/
# 1) add df.set_value, know how to use defaultdict know how to use df.iterrows()
# 2） pandas iat[]
# originally DataFrame.set_value(index, col, value, takeable=False)
# 3) pandas df.loc
# 4) from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
# 5) cross_val_score usage
###############################################################################################################

import pandas as pd
import numpy as np
from collections import defaultdict

df1 = pd.read_csv('nyc_weather.csv')
print(df1)
print( df1['Temperature'].max()          )
print( df1['EST'][df1['Events']=='Rain'] )

#optional (which fill naN with 0)
df1.fillna(0, inplace=True)
print(df1)
print( df1['WindSpeedMPH'].mean()        )

##################################################################################
df2 = pd.read_csv('weather_data.csv')
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df2 = pd.DataFrame(weather_data)
print(df2)
print('\n')
print(df2.shape)

print(df2.head())
print('\n')
print(df2.head(2))
print('\n')
print(df2.head(1))
print('\n')
print(df2.tail())
print('\n')
print(df2.tail(2))
print('\n')
print(df2.tail(1))

print(df2[1:3])
print('\n')
print(df2[0:2])

print(df2.columns)

print( df2['day'] )
print('\n')
print( type(df2['day']))
print('\n')
print( df2[['day','temperature']]  )
print('\n')

print(df2['temperature'].max())
print('\n')
print(df2[df2['temperature']>32])
print('\n')
print(df2[df2['temperature']==df2['temperature'].max()])
print('\n')
print(df2.describe())
print(df2['temperature'].std)
print(df2['event'].max())


print( df2.set_index('day'))
print('\n')
print(df2)
df2.set_index('day',inplace=True)
print(df2)
print('\n')

print(df2.index)
print('\n')
#df2.set_index('day',inplace=True)
print(df2.loc['1/2/2017'])
print('\n')

df2.reset_index(inplace=True)
print(df2.head())
print('\n')

df2.set_index('event',inplace=True)
print(df2)
print('\n')
df2.loc['Snow']

#1) how to use set_value -- replace the designated position by a specific number
df100 = pd.DataFrame({"A": [1, 5, 3, 4, 2],
                   "B": [3, 2, 4, 3, 4],
                   "C": [2, 2, 7, 3, 4],
                   "D": [4, 3, 6, 12, 7]})
df100.set_value(2, 'B', 100)
print(df100)
print('\n')
###2) but for 1) set_value is deprecated right now please use iat or at
## continued use example above
df101 = pd.DataFrame({"A": [1, 5, 3, 4, 2],
                   "B": [3, 2, 4, 3, 4],
                   "C": [2, 2, 7, 3, 4],
                   "D": [4, 3, 6, 12, 7]})
df101.iat[2,1] = 100
print(df101)
print('\n')
###3) about how to use df.loc
print(df101.loc[2]) ## this line can show which position has 2
print('\n')
print(df101.loc[[1,2]])## display content in row 1 and row 2
print('\n')
print(df101.loc[1:2,'B']) ## display content in row 1 and row 2 and also in column B
print('\n')
print(df101.loc[df101['B']>10]) ## display the row which B is bigger than 10
## and there are other instructions that won't be included in this file

###1) what is defaultdict(int)
#     what is iterrows()



###4) pandas_get_dummies
s = pd.Series(list('abca'))
print('\n')
print(pd.get_dummies(s)) ## create some identity matrix follow the sequence of abca
s1 = ['a','b',np.nan]
print('\n')
print(pd.get_dummies(s1))
print('\n')
print(pd.get_dummies(s1,dummy_na=True))
print('\n')
df22 = pd.DataFrame({'A':['a','b','a'],'B':['b','a','c'],'C':[1,2,3]})
print(pd.get_dummies(df22,prefix=['col1','col2']))
print('\n')
print(pd.get_dummies(pd.Series(list('abcaa'))))
print('\n')
print(pd.get_dummies(pd.Series(list('abcaa')),drop_first=True))
print('\n')
print(pd.get_dummies(pd.Series(list('abc')),dtype=float))

###5) cross_val_score usage


