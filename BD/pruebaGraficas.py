import mysql.connector 
import pandas as pd
import matplotlib.pyplot as plt


conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootroot",
    db = 'world'
)


#cursor = conexion.cursor()
query = '''
    select code as codigo, name as nombre, Continent as continente, Population as poblacion
    from country c 
    order by c.Population desc
    LIMIT 10
    ;
    '''
top10Grandes = pd.read_sql_query(query, conexion) #funcion de pandas p ahorrarme el cursor

top10Grandes.plot(x="nombre", y="poblacion", kind="barh", figsize=(10,5), legend=False)

plt.title('10 paises mas poblados')
plt.xlabel('Paises')
plt.ylabel('Poblacion')

print(top10Grandes)







