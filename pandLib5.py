import pandas as pd
diccionario = {
    'Nombre': ['María', 'María','María','Juan','Juan','Juan','Tomás','Tomás','Tomás'],
    'Fecha': ['06/06/2022','07/06/2022','07/06/2022','06/06/2022','07/06/2022','07/06/2022','06/06/2022','07/06/2022','07/06/2022'],
    'Cantidad': [8,2,8,1,5,8,5,8,7]
}
   
# método pivot_table
df1 = pd.DataFrame(diccionario) 
print(df1)
pt = pd.pivot_table(df1, index=['Nombre'], columns=['Fecha'], aggfunc=['sum','count'])
print(pt)
print(type(pt))
    