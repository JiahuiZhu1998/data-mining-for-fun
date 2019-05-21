################################################################################################
#Python version3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)]
#Pandas version0.24.2
#Matplotlib version3.0.3

# remember to pip install openpyxl
# remember to pip install xlrd
################################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib
import xlrd

#%matplotlib inlines
print('Python version'+sys.version)
print('Pandas version'+pd.__version__)
print('Matplotlib version' + matplotlib.__version__)
print('\n')

## set numpy seed
np.seed(111)

def createDataSet(Number=1):
    output = []
    for i in range(Number):
        rng = pd.date_range(start='1/1/2009',end='12/31/2012',freq='W-MON')##create weekly(mondays)date range
        date = np.randint(low=25,high=1000,size=len(rng))##create random date
        #print(date)
        status = [1,2,3] ## status pool
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]## make a random list of status
        states = ['GA','FL','fl','NY','NY','TX'] ## state pool
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]
        output.extend(zip(random_states,random_status,date,rng))

        return output

dataset = createDataSet(4)
#print(dataset)
df1 = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
print('\n')
print(df1.info())
print('\n')
print(df1.head())

## save results to excel
df1.to_excel('Lesson3.xlsx',index=False)
print('\n')
print('Done')

##grab data from excel
location = r'C:/Users/garry/Documents/data-mining-for-fun/005. pandas code intro/Lesson3.xlsx'
df2 = pd.read_excel(location,0,index_col='StatusDate')
print('\n')
print(df2.dtypes)
print('\n')
print(df2.index)
print('\n')
print(df2.head())
print('\n')
print(df2['State'].unique())
print('\n')
df2['State'] = df2.State.apply(lambda x: x.upper())
print(df2['State'].unique())
print('\n')
mask = df2['Status']==1
df2 = df2[mask]

#Convert NJ to NY
mask = df2.State =='NJ'
df2['State'][mask] = 'NY'
print(df2['State'].unique())
print('\n')
df2['CustomerCount'].plot(figsize=(15,5))
plt.show()
sortdf = df2[df2['State']=='NY'].sort_index(axis=0)
print(sortdf.head(10))
print('\n')

##Group by State and StatusDate
Daily = df2.reset_index().groupby(['State','StatusDate']).sum()
print(Daily.head())
print('\n')
del Daily['Status']
print(Daily.head())
print('\n')
print(Daily.index)
print('\n')
print(Daily.index.levels[0])
print('\n')
print(Daily.index.levels[1])
print('\n')
Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot()
plt.show()
Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot()
