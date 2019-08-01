import pandas as pd

# %% Series
h = ('AA', '2012-02-01', 100, 10.2);h
s = pd.Series(h)     # Note that tuple conversion, the index are set to 0,1,2,3:
type(s)
print(s)
f = pd.Series(h, index = ['name', 'date', 'shares', 'price'])
type(f)
print(s)

d = {'name': 'IBM', 'date': '2010-09-08', 'shares': 100, 'price': 10.2}
ds = pd.Series(d)
print(ds)

print(ds)
ds[0]
ds["shares"]
ds[["shares","price"]]   #if selecting multiple elements, use [[]]

# %% DataFrame- Creation
data = {'name': ['AA', 'IBM', 'GOOG'],
        'date': ['2001-12-01', '2012-02-10', '2010-04-09'],
        'shares': [100, 30, 90],
        'price': [12.3, 10.3, 32.2]}
type(data)
df=pd.DataFrame(data); type(df);
df

df["owner"]="Unknown";df                # creating additional columns

df.index=["One", "Two", "Three"];df     # Setting new row indices
df=df.set_index(["name"]);df            # Setting a current column as the DF indice


# %% DataFrame- Accessing
print(df)
df["shares"]

df.loc[:,"shares"]         # loc uses strings: [row,column] pair
df.loc["AA","date"]
df.iloc[:,0]               # iloc uses numbers



