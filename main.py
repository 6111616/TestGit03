import pandas as pd
#Class construtor:
data = {'Country': ['Thailand',  'India',  'Brazil'],
        'Capital': ['Bangkok',  'New Delhi',  'Brasilia'],
        'Population': [7160000, 1303171035, 207847528]}

#Inhrtitsnce:
df = pd.DataFrame(data ,columns=['Country',  'Capital',  'Population'])
df_sub = df[['Capital'  ,'Population']]

class MyDF(pd.DataFrame):
    @property
    def _constructor(self):
        return MyDF


print(str(df))
print(df_sub)

#Polymorphism
print(df.info(verbose=False))
print(df.info())