#%% Admin
import os
import pandas as pd
import numpy as np

os.getcwd()
DataFolder= "C:\\Users\\AndrewYeo\\Documents\\GitHub\\Personal_Cookbooks\\Cookbooks_Python\\DataFolder\\"

#%% Pandas Intro
Df1= pd.read_csv(DataFolder+"zoo.csv")
Df2= pd.read_csv(DataFolder+"pandas_tutorial_read.csv", delimiter=";",
            names=['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

Df2.head()
Df2.tail()
DfColumns=Df2.columns.values
Df2[['country', 'user_id']]    # note the double brackets
type(Df2[['country', 'user_id']])

Df2[["user_id"]]
Df2.user_id  # note that this is a series

# Subsetiing
Df2.source=="SEO"
Df2[Df2.source=="SEO"]



