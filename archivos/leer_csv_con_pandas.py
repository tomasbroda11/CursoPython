import pandas as pd

df = pd.read_csv("archivos\\tabla1.csv", names = ["Name","Lastname","age"]) 


#leyendo la columna nombre
nombres = df["Name"]

#print(df) 

#ordenando el datframe por valores
df_ordenado = df.sort_values("age")
print(df_ordenado)

#ordenandolo descendente 
df_ordenado_des = df.sort_values("age", ascending=False)
print(df_ordenado_des)

#concatenando los dos data frames
#df_concatenado = pd.concat(df, df2)

#accediendo al a primer fila con head()
primer_fila = df.head(1)
print(primer_fila)

#accedienfo a la ultima fila 
ult_fila = df.tail()

