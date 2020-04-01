import pandas as pd
from pandas import DataFrame
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from itertools import permutations

data=yf.download("VBIV",start='2019-01-01',end='2020-03-29')

#data=data.reset_index()


ma_list = [2,4,6,8,10,12,14]
perm=permutations([2,4,6,8,10,12,14],2)

pct_c=data.Close.pct_change


ma_array=[]

for i in list(perm):
    x,y = i
    if x > y:
        continue
    ma_array.append(i)

# calculate all the difference moving averages and store
shortma=[]
longma=[]

for i,j in ma_array:
    shortma.append(data.Close.rolling(window=i).mean())
    longma.append(data.Close.rolling(window=j).mean())

# create new list to contain results
diff=[]
zip_object=zip(shortma,longma)
for shortma_i,longma_j in zip_object:
    diff.append(shortma_i-longma_j)

#Create DataFrame with difference of SMA-LMA/If (+) then SMA > LMA
data1=pd.DataFrame(index=data.index)
data1=pd.DataFrame(diff)
data1=np.transpose(data1)
data1.columns=ma_array

data1['Close1']=data.Close

# change df values to rep 1 if +, 0 if -
#for col in data1.columns:
 #   data1[col] = np.where(data1[col] > 0,1, 0)

for col in data1.columns:
    data1[col]=np.where(data1[col]>0,data1['Close1'],0)



data1.reset_index(inplace = True)
data.reset_index(inplace = True)






    


    

       


    

#export_csv=data2.to_csv(r'C:\Users\hsman\Desktop\Python\practice\mine.csv',index=True,header=True)
#export_csv=data.to_csv(r'C:\Users\hsman\Desktop\Python\practice\testf.csv',index=True,header=True)







