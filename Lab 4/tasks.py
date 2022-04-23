import pandas as pd

df = pd.read_csv('dataset_lab04.csv')
#%%
# 1
print(f'Number of rows: {df.shape[0]}')
print(f'Number of columns: {df.shape[1]}')

#%%
# 2
print(df.describe())

#%%
# 3
print("Mean of every column:")
print(df.mean())

print("\nMedian of every column:")
print(df.median())

print("\nStandard deviation of every column:")
print(df.std())

print("\nVariance of every column:")
print(df.var())

#%%
# 4
import task4module
df4 = df['Time'] 
print(f'Mean from Pandas : {df4.mean()}')
print(f'Mean from Module: {task4module.mean(df4)}')

#%%
# 5
df.hist(column = ['Time'], xrot=90, bins=20)
df.hist(column = ['Amount'], xrot=90, bins=20)

#%%
# 6
df6 = df['Class']
total_count = df6.count()
percent_of_0 = df6.value_counts().get(0) / total_count
percent_of_1 = df6.value_counts().get(1) / total_count
print(f'Percentage of rows with class value 0 (Non-Fraudulent) : {percent_of_0 * 100}')
print(f'Percentage of rows with class value 1 (Fraudulent): {percent_of_1 * 100}')

#%%
# 7
df7 = pd.DataFrame({"label" : ['Fraud', 'Non Fraud'], "val" : [percent_of_1, percent_of_0]})
df7.plot.bar(x = 'label', y= 'val', rot = 0)
#%%
# 8
df['V1'].plot.hist()
df['V2'].plot.hist()
df['V3'].plot.hist()
#%%
# 9
df9 = df.corr()
df9 = df9[df9>0]
print(df9)
#%%
# 10
df9.plot.box()
#%%
# 11
df9.plot.scatter(x='V1',y='V2',c='black')

#%%
# 12
df12 = df.corr()
df12 = df12[df12<0]
print(df12)
#%%
# 13
df12.plot.box()
#%%
# 14
df12.plot.scatter(x='V1',y='V3',c='black')

