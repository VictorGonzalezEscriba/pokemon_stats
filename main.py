import pandas as pd   #importing all the important packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

df =  pd.read_csv('Pokemon.csv')  #read the csv file and save it into a variable
df.columns = df.columns.str.upper().str.replace('_', '') #change into upper case
df.head(n=10)    

#df.index = df.index.str.replace(".*(?=Mega)", "")
#df.index = df.index.str.replace(".*(?=Primal)", "")
#df.head(5)

df=df.drop(['#'],axis=1)
df['TYPE 2'].fillna(df['TYPE 1'], inplace=True) 

values_type_1 = df['TYPE 1'].value_counts()
for key, value in values_type_1.items():
    print("Keys: ", key)
    print("Value: ", value)
