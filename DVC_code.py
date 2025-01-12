import pandas as pd
import os

data={'Name':['Alice','sam','elon'],
      'Age':[25,30,35],
      'City':['us','uk','india']}

df=pd.DataFrame(data)



#Ensure the data directory exists at the root level

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#Define the file path

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"cvs file saved to {file_path}")