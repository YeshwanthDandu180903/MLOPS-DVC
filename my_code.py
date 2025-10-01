import os
import pandas as pd

data={'Name':['Yeshwanth','Lohith','Arun','Nikhith'],'Age':[21,22,20,21],'City':['Hyderabad','Kerala','Pondicherry','Shanghai']}

df=pd.DataFrame(data)

#adding one row to df  for V2
new_row_loc={'Name':'Vrindha','Age':22,'City':"Madurai"}
df.loc[len(df.index)]=new_row_loc

#creating a data directory for storing the data
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#defining the path
file_path=os.path.join(data_dir,'sample_data.csv')

#save the dataframe to a csv file,including column names
df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")
