import mysql.connector
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootroot",
    db = 'Nombre de la base'
)

cursor = conexion.cursor()

cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
