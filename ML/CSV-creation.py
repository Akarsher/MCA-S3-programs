import pandas as pd
import numpy as np

data = {'Name' :['akarsh','akhil','adwaith','adithya','allen'],
        'Age' :[21,22,20,22,23],
        'Course' :['B.Tech','M.Tech','Bsc-CS','MCA','BCA']}
df = pd.DataFrame(data)
print(df)

df.to_csv('data.csv',index=False)
print("CSV file created successfully.")
