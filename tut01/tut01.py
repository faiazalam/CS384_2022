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
    table1=[]
table2=[]
table3=[]
octant=[]
for i in df['U']:
    table1.append(i-avgu)
for i in df['V']:
    table2.append(i-avgv)
for i in df['W']:
    table3.append(i-avgw)

df["U'=U - U avg"]=table1
df["V'=V - V avg"]=table2
df["W'=W - W avg"]=table3


c1=c11=c2=c22=c3=c33=c4=c44=0
for p in range(len(df['U'])):
    if table1[p]>=0 and table2[p]>=0 :
        if table3[p]>=0 :
            octant.append(1)
            c1+=1
        else:
            octant.append(-1)
            c11+=1
    if table1[p]<0 and table2[p]>=0 :
        if table3[p]>=0 :
            octant.append(2)
            c2+=1
        else:
            octant.append(-2)
            c22+=1
    if table1[p]<0 and table2[p]<0 :
        if table3[p]>=0 :
            octant.append(3)
            c3+=1
        else:
            octant.append(-3)
            c33+=1
    if table1[p]>=0 and table2[p]<0:
        if table3[p]>=0 :
            octant.append(4)
            c4+=1
        else:
            octant.append(-4)
            c44+=1

df["octant"]=octant
one=[]
mone=[]
two=[]
mtwo=[]
three=[]
mthree=[]
four=[]
mfour=[]
count=0
one.append(c1)
mone.append(c11)
two.append(c2)
mtwo.append(c22)
three.append(c3)
mthree.append(c33)
four.append(c4)
mfour.append(c44)
octantID=["Overall count"]
flag=0

while True:
    c1=c11=c2=c22=c3=c33=c4=c44=0
    num = count + mod
    numI = count + 1
    if (count + mod) > 29746:
        num = 29746
    if count == 0:
        numI = 1
    octantID.append(f"{numI-1} - {num-1}")

    for i in range(count,count+mod):
        if i >= len(df['U']):
            flag = 1
            break
        if octant[i] == 1:
            c1+= 1
        if octant[i] == -1:
            c11 += 1
        if octant[i] == 2:
            c2 += 1
        if octant[i] == -2:
            c22 += 1
        if octant[i] == 3:
            c3 += 1
        if octant[i] == -3:
            c33 += 1
        if octant[i] == 4:
            c4 += 1
        if octant[i] == -4:
            c44 += 1
        count += 1
    
    one.append(c1)
    mone.append(c11)
    two.append(c2)
    mtwo.append(c22)
    three.append(c3)
    mthree.append(c33)
    four.append(c4)
    mfour.append(c44)
    if flag == 1:
        break

for i in range(len(octantID)):
    j = i
    df.loc[i,"OctantID"]=octantID[i]
    df.loc[i,"1"]=one[j]
    df.loc[i,"-1"]=mone[j]
    df.loc[i,"2"]=two[j]
    df.loc[i,"-2"]=mtwo[j]
    df.loc[i,"3"]=three[j]
    df.loc[i,"-3"]=mthree[j]
    df.loc[i,"4"]=four[j]
    df.loc[i,"-4"]=mfour[j]


# print(df.head())
for i in range(len(octantID)):
    print(octantID[i],"       ",one[i]," ",mone[i]," ",two[i]," ",mtwo[i]," ",three[i]," ",mthree[i]," ",four[i]," ",mfour[i])

df.to_csv("octant_output.csv",index=False)


