import csv
import pandas as pd
import numpy as np

data=pd.read_csv("fdx_1.csv")

ORIG=data['ORIGIN']
SCAN=list(data['SCAN LOCATION'])
TYPE=data['SORT TYPE']


data['test']=np.where(ORIG == 753, "DALL", "Not")
data['dup']=data.groupby(['TRKID']).cumcount()+1
data['test2']=np.where(data["SCAN LOCATION"].shift(-1) == 753, "To DALL",
                       np.where(data["SORT TYPE"] == "}","To Station","Not"))

result=[]
for value in ORIG:
    if value == 753:
        result.append("DALL")
    else:
        result.append("Not DALL")
data['Result']=result

new=[]
for i in range(0,len(SCAN)):
    if SCAN[i+1] == 753:
        new.append("IN DALL")
    else:
        new.append("Not")


#LOCA = data[data['SCAN LOCATION'] == 753]
#datindex=LOCA.index    
#din=LOCA.index-1


export_csv=data.to_csv(r'C:\Users\2795403\Desktop\Python\fdx.csv',index=True,header=True)
