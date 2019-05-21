#from https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/02%20-%20Lesson.ipynb
#python 3.7
#5/20/2019
#Jiahui Zhu
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys
import matplotlib
## enable inline plotting
#%matplotlib inline

print('Python version'+sys.version)
print('Pandas version'+pd.__version__)
print('Matplotlib version' + matplotlib.__version__)

###To make a random list of 1,000 baby names
names = ['Bob', 'Jessica','Mary','John','Mel']
random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]
print(random_names[:10])
### Generate a random numbers between 0 and 1000
births = [random.randint(low=0,high=1000) for i in range(1000)]
print(births[:10])
#Merge the names and the births data set using the zip function.
BabyDataSet =list(zip(random_names,births))
print(BabyDataSet[:10])

## create dataframe about babydataset
df1 =pd.DataFrame(data=BabyDataSet, columns=['Names','Births'])
print(df1[:10])
## export dataframe to a text file
df1.to_csv('birth1880.txt',index=False,header=False)
## get data from a text file
location = r'C:/Users/garry/Documents/data-mining-for-fun/005. pandas code intro/birth1880.txt'
df2 = pd.read_csv(location)
print(df2)
print(df2.info())
print(df2.head())
df3 = pd.read_csv(location,header=None)
print(df3.info())
print(df3.tail())
df4 = pd.read_csv(location,names=['Names','Births'])
print(df4.head())

# import os
# os.remove(location)

#####Prepare data
print(df4['Names'].unique())
for name in df4['Names'].unique():
    print(name)
print('\n')
print(df4['Names'].describe())

name = df4.groupby('Names')
df5 = name.sum()
print(df5)

#####Analyze data
## sorted
print('\n')
sorted = df5.sort_values(['Births'],ascending=False)
print(sorted.head())
print('\n')
print(df5['Births'].max())
#####Present data
df5['Births'].plot.bar()
plt.show()
print('The most popular name')
print(df5.sort_values(by='Births',ascending=False))