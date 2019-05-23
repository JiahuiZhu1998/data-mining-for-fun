################################################################################################
# Python version3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
# Pandas version0.24.2
# Matplotlib version3.0.3
# Name:Jiahui Zhu
# Date: 5/22/2019
# from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/03%20-%20Lesson.ipynb
# remember to pip install openpyxl
# remember to pip install xlrd
## do not understand: Daily = df2.reset_index().groupby(['State','StatusDate']).sum()
##
################################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

#%matplotlib inlines
print('Python version'+sys.version)
print('Pandas version'+pd.__version__)
print('Matplotlib version' + matplotlib.__version__)
print('\n')

## set numpy seed
np.seed(111)

def createDataSet(Number=1):
    output = []
    ###randint() can create random numbers
    for i in range(Number):
        rng = pd.date_range(start='1/1/2009',end='12/31/2012',freq='W-MON')##create weekly(mondays)date range
        date = np.randint(low=25,high=1000,size=len(rng))##create random integer number
        status = [1,2,3] ## status pool
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]## make a random list of status
        states = ['GA','FL','fl','NY','NJ','TX'] ## state pool
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
        ## extend means no bruckets. it will combine elements in the list into another list
        output.extend(zip(random_states,random_status,date,rng))
        #print(output)
        return output

dataset = createDataSet(4)
df1 = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
print('\n')
### df1.info is different from instructions
print(df1.info())
print('\n')
print(df1.head())



## save results to excel
df1.to_excel('Lesson3.xlsx',index=False)
print('\n')
print('Done')
print('\n')
print('Part1 has ended!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
##grab data from excel
location = r'C:/Users/garry/Documents/data-mining-for-fun/001. pandas code intro/Lesson3.xlsx'
### read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None,names=None, parse_cols=None, parse_dates=False,date_parser=None,na_values=None,thousands=None, convert_float=True, has_index_names=None, converters=None,dtype=None, true_values=None, false_values=None, engine=None, squeeze=False, **kwds)
df2 = pd.read_excel(location,0,index_col='StatusDate')
print('\n')
print(df2.dtypes)
print('\n')
### show all 'StatusDate' in a list
print(df2.index)
print('\n')
print(df2.head())
print('\n')
print('Start to prepare data!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('\n')
#### see how many different states appears in the dataframe
print(df2['State'].unique())
print('\n')
### change all lower cases to upper case and display the list again
df2['State'] = df2.State.apply(lambda x: x.upper())
print(df2['State'].unique())
print('\n')
############only when Status is equal to 1 and grab
df2 = df2[df2['Status']==1]
#print(df2)
print('\n')
#Convert NJ to NY
df2['State'][df2.State =='NJ'] = 'NY'
print(df2['State'].unique())
print('\n')
### the figure which is (15,5) is not same as instruction
df2['CustomerCount'].plot(figsize=(15,5))
#plt.show()
#print(df2[df2['State']=='NY'])
### sortdf is not same as instruction's
#DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)
sortdf = df2[df2['State']=='NY'].sort_index(axis=0)
print(sortdf.head(10))
print('\n')

##Group by State and StatusDate
print(df2.reset_index())
## the result is not same as instruction
Daily = df2.reset_index().groupby(['State','StatusDate']).sum()
print(Daily.head())
print('\n')
print('start to delete!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('\n')
del Daily['Status']
print(Daily.head())
print('\n')
print(Daily.index)
print('\n')
print(Daily.index.levels[0])### State which is same as instruction
print('\n')
print(Daily.index.levels[1]) ###StatusDate same as instruction
print('\n')
#### these four plots are not same as instructions
# print(Daily.loc['FL'])
# print('\n')
# print(Daily.loc['GA'])
Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot()
#plt.show()
#### these four plots are not same as instructions
Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot()

StateYearMonth = Daily.groupby([Daily.index.get_level_values(0),Daily.index.get_level_values(1).year,Daily.index.get_level_values(1).month])
print(StateYearMonth)
"""
Daily['Lower'] = StateYearMonth['CustomerCount'].transform(lambda x:x.quantile(q=.25)-(1.5*x.quantile(q=.75)-x.quantile(q=.25)))
Daily['Upper'] = StateYearMonth['CustomerCount'].transform(lambda x:x.quantile(q=.75)+(1.5*x.quantile(q=.75)-x.quantile(q=.25)))
Daily['Outlier'] = (Daily['CustomerCount']<Daily['Lower']) | (Daily['CustomerCount']>Daily['Upper'])
###
Daily=Daily[Daily['Outlier']==False]
print(Daily.head())

###Combine all markets
ALL =pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount']
#Group by Year and Month
YearMonth=ALL.groupby([lambda x:x.year, lambda x:x.month])
# What is the max customer count per Year and Month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x:x.max())
print(ALL.head())

#######################
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011',end='12/31/2013',freq='A')
BHAG = pd.DataFrame(data,index=idx,columns=['BHAG'])
print('\n')
print(BHAG)
#######################
combined = pd.concat([ALL,BHAG], axis=0)
combined = combined.sort_index(axis=0)
print('\n')
print(combined.tail())
#######################
fig,axes = plt.subplots(figsize=(12,7))

combined['BHAG'].fillna(method='pad').plot(color='green',label='BHAG')
combined['Max'].plot(color='blue',label='All Markets')
plt.legend(loc='best')
plt.show()
print('\n')
###Group by Year and then get the max value per year
Year = combined.groupby(lambda x:x.year).max()
print(Year)
print('\n')
##Add a column representing the percent change per year
Year['YR_PCT_Change']= Year['Max'].pct_change(periods=1)
print(Year)
print('\n')
#####
print( (1+Year.loc[2012,'YR_PCT_Change'])*Year.loc[2012,'Max'])

####present data
ALL['Max'].plot(figsize=(10,5));plt.title('All Markets')
#Last four Graphs
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(20,10))
fig.subplots_adjust(hspace=1.0)##Create space between plots

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,1])
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,0])
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1,1])

##Add titles
axes[0,0].set_title('Florida')
axes[0,1].set_title('Gerogia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East')
"""