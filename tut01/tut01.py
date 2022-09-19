import csv
#using csv library
import pandas as pd
#installing pandas library for manipulating all the data

df=pd.read_csv("octant_input.csv",'r')
#reading csv file
mod = int(input("Enter mod - "))

avgu=df['U'].mean()
avgv=df['V'].mean()
avgw=df['W'].mean()
#finding average of all the U,V,W
df.loc[0,'U Avg']=avgu
df.loc[0,'V Avg']=avgv
df.loc[0,'W Avg']=avgw
    
