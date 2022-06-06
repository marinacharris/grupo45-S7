import pandas as pd
df1 = pd.read_csv('surveys.csv')
print(df1.head(15)) # imprime las primeras 15 líneas
print(df1.tail(10)) # imprime las ultimas 10 líneas
print(df1.shape)
print(df1.columns)
print(pd.unique(df1['species_id'])) # imprime un lista de los datos únicos de una columna
print(df1['species_id'].value_counts()) #cuenta los datos únicos de una columna
print(df1['weight'].describe())
print(df1['weight'].mean())
print(df1.groupby('species_id')['record_id'].count()['AH'])



