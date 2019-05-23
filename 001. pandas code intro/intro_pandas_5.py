####################################################################################################################
#  Python version3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
#  Pandas version0.24.2
#  Matplotlib version3.0.3
#  Name: Jiahui Zhu
#  some questions need to comprehensive below:
#  from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/04%20-%20Lesson.ipynb
#  from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/05%20-%20Lesson.ipynb
#  from https://blog.csdn.net/starter_____/article/details/79183733                1)
#  from https://blog.csdn.net/xueruixuan/article/details/81451690                  2)
#   from https://blog.csdn.net/youngbit007/article/details/54288603/                2)
#  from https://blog.csdn.net/AnneQiQi/article/details/71057069                    3)
#  from http://www.30daydo.com/article/257                                         4)
#  from https://blog.csdn.net/cdpxc/article/details/81633661                       5)
#  from https://blog.csdn.net/orangefly0214/article/details/81108649               6)
#  from https://blog.csdn.net/zwhooo/article/details/79696558                      7)
#  from https://www.jianshu.com/p/f0ed06cd5003                                     8)
#  from https://blog.csdn.net/weixin_38168620/article/details/79596819             9)
#  from https://blog.csdn.net/mr_hhh/article/details/79488445                      10)
#
#  get to know what .stack and .unstack mean in dataframe
#####################################################################################################################
import pandas as pd
import sys
import numpy as np
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
print('\n')
####1)################### how to use sort_value & sort_index
print('Problem 1 shows below')
df55 =pd.DataFrame(np.arange(12).reshape((4,3)),columns=['c','a','b'],index=['D','B','C','A'])
print(df55)
print('\n')
print(df55.sort_index(axis=0)) ## descending by y axis
print('\n')
print(df55.sort_index(axis=1)) ## ascending by y axis
print('\n')
print(df55.sort_index(axis=1,ascending=False))
print('\n') ## ascending controls horizontally sorting sequence
####2)################### how to use groupby in pandas and save data to the dataframe
print('Problem 2 shows below:')
### compare df56 and df57
df56 = pd.DataFrame({'a':[1,1,3,2],'b':[1,4,6,9],'c':[1,4,8,12]})
print(df56)
print('\n')
df57 = pd.DataFrame({'a':[1,1,3,2],'b':[1,1,6,9],'c':[1,4,8,12]})
print(df57)
print('\n')
g_df = df56['c'].groupby([df56['a'],df56['b']]).sum()
print(g_df)
print('\n')
d_df = df57['c'].groupby([df57['a'],df57['b']]).sum()
print(d_df)
print('\n')
end_df = pd.DataFrame(g_df)
print(end_df)    ## save all data of g_df to end_df and arrange data by index and columns
print('\n')
end_df.reset_index(inplace=True)
print(end_df)    ## back to the original condition
print('\n')
### the second website
df58 = pd.DataFrame({'key1':list('aabba'),
                  'key2': ['one','two','one','two','one'],
                  'data1': np.random.randn(5),
                  'data2': np.random.randn(5)})
print(df58)
print('\n')
group58 = df58['data1'].groupby(df58['key1']).mean()
print(group58)
print('\n')
####6)###################################how to use transform function in pandas
print(df58['data1'].groupby(df58['key1']).transform(np.mean))
print('\n')
##########end of question 6 ----> it just fill content in each space(eg. np.mean)
state58=np.array(['Ohio','California','California','Ohio','Ohio'])
year58=np.array([2005,2005,2006,2005,2006])
print(df58['data1'].groupby([state58,year58]).mean())
print('\n')
print(df58.groupby('key1').mean())
print('\n')
###
for name,group in df58.groupby('key1'): ### for names in key1
    print('\n')
    print(name)
    print('\n')
    print(group)
print('\n')
###
for(k1,k2),group in df58.groupby(['key1','key2']): ## show each row in each time
    print('\n==k1,k2')
    print('\n')
    print(k1,k2)
    print('\n==k3')
    print('\n')
    print(group)
###### other content in the second website will not be included in this script

####3)########################## usage of remove,del and pop
print('\n')
a59 = [1,2,3]
a59.remove(2)
print(a59)
a59_2 = [1,2,3]
del a59_2[1]
print('\n')
print(a59_2)
print('\n')
a59_3 = [1,2,3]
print(a59_3.pop(2))
print(a59_3)
print('\n')
####4)########################### dataframe reindex and reset_index usage of cancat
df60 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
df60_2 = pd.DataFrame({'A': [6], 'B': [60]})
print(df60)
print('\n')
print(df60_2)
print('\n')
df_x60 = [df60,df60_2]
### concat is to combine two dataframe together
result60 = pd.concat(df_x60) ## the index of result60 is not excellent
print(result60)
print('\n')
result60_2 = result60.reset_index() ## assign new index but does not change sequence
print(result60_2)
print('\n')
result60_3 = result60.reset_index(drop=True) ####assign new index and replace the original one
print(result60_3)
print('\n')
result60_4 = result60.reindex(columns = ['A','C']) ## only show content in columns and also replace the sorted index
print(result60_4)

####5)###################################some simple python guidance
#df61

####6)###################################how to use transform function in pandas
### in questions above

####7)###################################how to use map,apply,transform,agg

## one column assigned operation called map
print('\n')
df62 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50],'C':[0,0,0,0,0]})
print(df62)
print('\n')
df62['C'] = df62['A'].map(lambda x: x**2)
print(df62)
## multuple column assigned opearation called apply
print('\n')
df62_2 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50],'C':[0,0,0,0,0]})
print('\n')
df62_2['C'] = df62_2.apply(lambda x: x['A'] + 2 * x['B'], axis=1) #C = 2*B+A
print(df62_2)
print('\n')
## use groupby.transform
df62_3 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50],'C':[0,0,0,0,0]})
df62_3['C'] = df62_3.groupby('A')['B'].transform(lambda x: (x.sum() - x) / x.count()) #<--------------- error
print(df62_3)
## use agg transform
df62_4 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50],'C':[0,0,0,0,0]})
#df62_4['C'] = df62_4.groupby(['A']).agg({'A':{'A_mean': mean, 'col1_sum‘’: sum}, 'col2': {'col2_count': count}})
##line above has error
####8)################################### about sort_index() and sort_value() which have been covered
pass;
####9)################################### about how to use fillna

####10)################################## details about how to use concat

