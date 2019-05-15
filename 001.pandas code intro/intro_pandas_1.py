import pandas as pd

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
df2.set_index('day',inplace=True)
print(df2.loc['1/2/2017'])
print('\n')

df2.reset_index(inplace=True)
print(df2.head())
print('\n')

df2.set_index('event',inplace=True)
print(df2)
print('\n')
df2.loc['Snow']