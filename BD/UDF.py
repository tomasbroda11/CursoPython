import mysql.connector
import pandas as pd

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootroot",
    db = 'world'
)
cursor = conexion.cursor()

cursor.execute(
    ''' 
    select code, name, Continent, Region
    from country c 
    where c.Code LIKE 'A%'
    ;
    
    ''')

resultado = cursor.fetchall()
resultado_df = pd.DataFrame(resultado)

conexion.commit() #GUARDO LOS CAMBIOS EN LA BD. Como estamos desde py los cambios q hagamos son de tipo transacciones

cursor.close()
conexion.close()
print(resultado_df)


