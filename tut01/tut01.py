import pandas as pd 
import numpy as np
df=pd.read_csv('octant_input.csv')


A=df['Time'].to_numpy()
B=df['U'].to_numpy()
C=df['V'].to_numpy()
D=df['W'].to_numpy()
        
m1=np.mean(A)     
P=A-m1
m2=np.mean(B)
Q=B-m2
m3=np.mean(C)
R=C-m3
m4=np.mean(D)
S=D-m4
def get_octant(pA,pB,pC,pD):
    for point in df:
        if P<0 & Q<0:
            if R<0 & S<0:
                print("first_octant")
            if(R<0 & S>0):
                print("second_octant")
            if(R>0 & S<0):
                print("third_octant")
            if(R>0 & S>0):
                print("tenth_octant")
        if P<0 & Q>0:
             if R<0 & S<0:
                print("fourth_octant")
                if(R<0 & S>0):
                    print("ninth_octant")
                    if(R>0 & S<0):
                        print("eleventh_octant")
                        if(R>0 & S>0):
                           print("fifteenth_octant")
        if P>0 & Q<0:
            if R<0 & S<0:
                print("fith_octant")
                if R<0 & S>0:
                    print("seventh_octant")
                    if R>0 & S<0:
                        print("eigth_octant")
            if R>0 & S>0:
                print("forteenth_octant")
        if P>0 & Q>0:
            if R<0 & S<0:
                print("sixth_octant")
                if R<0 & S>0:
                    print("thirteenth_octant")
                    if R>0 & S<0:
                        print("twethth_octant")
                        if R>0 & S>0:
                            print("sixteenth_octant")