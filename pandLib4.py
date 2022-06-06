import pandas as pd
df1 = pd.read_csv('surveys.csv')
print(df1.columns)
df2 = df1['month'] #se crea un subconjunto de una columna que es una serie
df3 = df1[['species_id', 'plot_id']] # se crea un subconjunto de varias columnas que es un dataframe
print(df2)
print(df3)
print(type(df2), type(df3))
print(df1.iloc[5]) # imprime la linea n de un dataframe
print(df1[10:21]) #formas distintas de obtener sectores del dataframe
print(df1.iloc[0:4,1:3])
print(df1.iloc[[0,5,8],:])
print(df1.iloc[8,7])
print(df1.loc[[2,5],['year','species_id']])
# filtros
print(df1[df1.year == 1977])
print(df1[(df1.year>= 1985) & (df1.year <= 1995) ])  # and: &, or:|, not:~







