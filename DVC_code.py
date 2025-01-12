import pandas as pd


import os

data={'Name':['Alice','sam','elon'],
      'Age':[25,30,35],
      'City':['us','uk','india']}

df=pd.DataFrame(data)

#Adding new row to the df for v2
new_row={'Name':'GF',
      'Age':20,
      'City':'BRAZIL'}
df.loc[len(df.index)]=new_row


#Adding new row to the df for v3
new_row={'Name':'GF1',
      'Age':21,
      'City':'up'}
df.loc[len(df.index)]=new_row



#Ensure the data directory exists at the root level

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"cvs file saved to {file_path}")