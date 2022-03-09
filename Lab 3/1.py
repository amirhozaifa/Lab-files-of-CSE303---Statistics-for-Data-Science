import pandas as pd

# 1
obj = pd.Series([4, 7, -5, 3])
print(obj[obj%2==0])
print(obj+5)
print(obj*2)

# 2
sdata = {'Ohio': 35000, 'Texas': 71000,
          'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)



# 3.1
list1 = [['Alice',23,3.5,10],
          ['Bob',24,3.4,6],
          ['Charlie',22,3.9,8]]
df = pd.DataFrame(list1)
df.columns = ['name','age','cgpa','hoursStudied']
print(df)

# # 3.2
dict1 = {'id':[1,2,3],
          'name':['alice','bob','charlie'],
          'age':[20, 25, 32]}
df1 = pd.DataFrame(dict1)
print(df1)

# # 3.3
df2 = pd.read_csv('sample_data_1.csv', 
                  header = None)
df2.columns=['id','state',
              'population',
              'murder_rate']
print(df2)
print(df2.head()) # displays first 5 rows
print(df2.tail()) # displays last 5 rows
print(df2.count()) # displays number of values for each column



# 4
print(df1.loc[0][1])
print(df1.iloc[0][1])
print(df1.loc[0]['name'])
print(df1.iloc[0]['name'])

df3=df[['name','cgpa']]
print(df[['name','cgpa']])

df4 = df2.loc[1:2]
print(df4)
df5 = df2.iloc[1:3]
print(df5)

df4 = df.loc[1:2,['name','age']]
print(df4)
df5 = df.iloc[1:3,[0,1]]
print(df5)

# append
list1 = [['Alice',23,3.5,10],['Bob',24,3.4,6],['Charlie',22,3.9,8]]
df = pd.DataFrame(list1)
df.columns = ['name','age','cgpa','hoursStudied']
list2 = [['Don',21,2.5,2],['Elton',25,2.75,4]]
df11 = pd.DataFrame(list2)
df11.columns = ['name','age','cgpa','hoursStudied']
df12 = df.append(df11, ignore_index=True)
print(df12)

# delete
df12.drop([0,1], inplace=True)
print(df12)
df12.drop(['cgpa'], axis=1, inplace=True)
print(df12)

# Rename
new_cols = ['n','a','hs']
df12.columns = new_cols
print(df12)



# 5
cgpa_greater_than_three_point_five1 = df[df['cgpa'] > 3.5]
cgpa_greater_than_three_point_five2 = df.loc[df['cgpa'] > 3.5]
cgpa_greater_than_three_point_five3 = df.query('cgpa > 3.5')

print(cgpa_greater_than_three_point_five1)
print(cgpa_greater_than_three_point_five2)
print(cgpa_greater_than_three_point_five3)
df.sort_values(by='age',ascending=False)
