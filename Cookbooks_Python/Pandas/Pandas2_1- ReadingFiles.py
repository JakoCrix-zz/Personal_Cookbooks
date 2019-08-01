import os
import pandas as pd

os.getcwd()
FileLocation='C:\\Users\\AndrewYeo\\Documents\\GitHub\\Personal_Cookbooks\\Cookbooks_Python\\Pandas\\DataFolder\\'

# %% Reading Files
casts= pd.read_csv(FileLocation+"cast.csv", index_col=None)