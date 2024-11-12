import pandas as pd
# nested dictionary
dic={
    'id':[1,2,3,4,5],
    'fname':['nimisha','nisa','mini','davis','shareef'],
    'lname':['davis','fendro','davis','kl','vc'],
    'age':[25,36,65,71,36],
    'location':['tvm','tcr','kasg','knr','kzhd']
}
# convert 2D data into DataFrame
df=pd.DataFrame(dic)
print(df)

# describe() : summarize output of each numerical columns
print(df.describe())

# datatype
print(df.dtypes)
# id           int64
# fname       object--- in pandas String col will always object
# lname       object
# age          int64
# location    object
# dtype: object

# to describe object only
print(df.describe(include='O'))

# describe all
print(df.describe(include='all'))
