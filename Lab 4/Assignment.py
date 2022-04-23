#%%
# Student ID: 2019-3-60-109
# Student Name: Md. Amir Hozaifa Bin Zaher
# Lab Assignment - 1

import pandas as pd
df = pd.read_csv('dataset_lab04.csv')
df.info()

#%%
# Task 1
def lab04_task1_2019_3_60_109():
    print(f'Number of rows: {df.shape[0]}')
    print(f'Number of columns: {df.shape[1]}')
    

#%%
# Task 2
def lab04_task2_2019_3_60_109():
    print(df['Time'].describe())
    print(df['Amount'].describe())
    

#%%
# Task 3
def lab04_task3_2019_3_60_109():
    print("Mean of Time column:")
    print(df['Time'].mean())
    
    print("\nMedian of Time column:")
    print(df['Time'].median())
    
    print("\nStandard deviation of Time column:")
    print(df['Time'].std())
    
    print("\nVariance of Time column:")
    print(df['Time'].var())


    print("Mean of Amount column:")
    print(df['Amount'].mean())
    
    print("\nMedian of Amount column:")
    print(df['Amount'].median())
    
    print("\nStandard deviation of Amount column:")
    print(df['Amount'].std())
    
    print("\nVariance of Amount column:")
    print(df['Amount'].var())
    

#%%
# Task 4
def statistical_values(df):
    q1 = df.quantile(.25)
    q2 = df.quantile(.5)
    q3 = df.quantile(.75)
    iqr = q3 - q1;
    print(f'Q1 :\t\t{q1}')
    print(f'Median :\t{q2}')
    print(f'Q3 :\t\t{q3}')
    print(f'IQR :\t\t{iqr}')
    
    mn = df.min()
    mx = df.max()
    lo = q1 - 1.5 * iqr;
    up = q3 + 1.5 * iqr;
# If max value is greater than upper fence
# or min value is less than lower fence,
# that means there are outliers
    if mn < lo or up < mx:
        print('There are outliers')
    else:
        print('There are no outliers')


def lab04_task4_2019_3_60_109():
    df[['Time', 'Amount']].plot.box()
    print('For time column: ')
    statistical_values(df['Time'])
    print('\nFor amount column: ')
    statistical_values(df['Amount'])

#%%
# Task 5
def skew_kurt(df):
    skw = df.skew()
    krt = df.kurt()
    print("Skewness: " , skw)
    print("Kurtosis: " , krt)
    print()
    if skw > 0:
        print('Positive Skew')
    elif skw == 0:
        print('Normal Distribution')
    else:
        print('Negative Skew')
        
    if krt > 3:
        print('Leptokurtic')
    elif krt == 3:
        print('Mesokurtic')
    else:
        print('Platykurtic')

def lab04_task5_2019_3_60_109():
    df.hist(column = 'Time')
    df.hist(column = 'Amount')
    print('For time column: ')
    skew_kurt(df['Time'])
    print('\nFor amount column: ')
    skew_kurt(df['Amount'])
    
#%%
# Task 6
df6 = df['Class']
total_count = df6.count()
percent_of_0 = df6.value_counts().get(0) / total_count
percent_of_1 = df6.value_counts().get(1) / total_count
def lab04_task6_2019_3_60_109():
    print(f'Percentage of rows with class value 0 (Non-Fraudulent) : {percent_of_0 * 100} %')
    print(f'Percentage of rows with class value 1 (Fraudulent): {percent_of_1 * 100} %')      

#%%
# Task 7
def lab04_task7_2019_3_60_109():
    df7 = pd.DataFrame({"label" : ['Fraud', 'Non Fraud'], "val" : [percent_of_1, percent_of_0]})
    df7.plot.bar(x = 'label', y= 'val', rot = 0)    

#%%
# Task 8
def lab04_task8_2019_3_60_109():
    df8 = pd.DataFrame({"label" : ['Fraud', 'Non Fraud'], "val" : [percent_of_1, percent_of_0]})
    df8.plot.bar(x = 'label', y= 'val', rot = 0)    

#%%
# Task 9
def lab04_task9_2019_3_60_109():
    # skw_v1 = df['V1'].skew()
    # skw_v4 = df['V4'].skew()
    # krt_v2 = df['V2'].kurt()
    # krt_v11 = df['V11'].kurt()
# Here,
# skw_v1 is -3.2806673027560405 (negative skew)
# skw_v4 is 0.676292097985747 (positive skew)
# krt_v2 is 95.7731059638466 (leptokurtic)
# krt_v11 is 1.6339212577978683 (platykurtic)
    df.hist(column = 'V1')
    df.hist(column = 'V4')
    df.hist(column = 'V2')
    df.hist(column = 'V11')
    

#%%
# Task 10
import numpy as np

corr = df.corr() 
# Since same columns generate 1 we need to
# remove them
np.fill_diagonal(corr.values, np.nan)
corr = corr.unstack()
largest = corr.nlargest(1)

def lab04_task10_2019_3_60_109():
    print(largest)
    

#%%
# Task 11
def lab04_task11_2019_3_60_109():
    df.plot.scatter(x='V7',y='Amount')
    

#%%
# Task 12
import numpy as np

corr = df.corr() 
# Since same columns generate 1 we need to
# remove them
np.fill_diagonal(corr.values, np.nan)
corr = corr.unstack()
smallest = corr.nsmallest(1)

def lab04_task12_2019_3_60_109():
    print(smallest)
    

#%%
# Task 13
def lab04_task13_2019_3_60_109():
    df.plot.scatter(x='V2',y='Amount')
    

#%%
# Task 14
def lab04_task14_2019_3_60_109():
    df.boxplot(column=['Amount'])
    

#%%
# Task 15
def lab04_task15_2019_3_60_109():
    df.boxplot(column='Amount', by='Class')
    print('''It is visible that most of the outliers are present in Non-Fraudulant (0) values.
We can also see that most number of values are also from Non-Fraudulant (0) values.''')
    

#%%
# Functions calls

#%%
# Task 1
lab04_task1_2019_3_60_109() 

#%%
# Task 2
lab04_task2_2019_3_60_109()  

#%%
# Task 3
lab04_task3_2019_3_60_109()

#%%
# Task 4
lab04_task4_2019_3_60_109()

#%%
# Task 5
lab04_task5_2019_3_60_109()

#%%
# Task 6
lab04_task6_2019_3_60_109()

#%%
# Task 7
lab04_task7_2019_3_60_109()

#%%
# Task 8
lab04_task8_2019_3_60_109()

#%%
# Task 9
lab04_task9_2019_3_60_109()    

#%%
# Task 10
lab04_task10_2019_3_60_109()
    

#%%
# Task 11
lab04_task11_2019_3_60_109()


#%%
# Task 12
lab04_task12_2019_3_60_109()

#%%
# Task 13
lab04_task13_2019_3_60_109()  

#%%
# Task 14
lab04_task14_2019_3_60_109() 

#%%
# Task 15
lab04_task15_2019_3_60_109()  