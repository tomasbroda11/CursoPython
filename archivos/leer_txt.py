archivo_sin_leer = open("archivos\\texto.txt", encoding="UTF-8")
##leer archivo completo
##archivo = archivo_sin_leer.read()

#leer linea por linea 
#lineas = archivo_sin_leer.readlines()

#leer una sola linea. 
# si no le pongo parametro al readline(), me lee toda la linea. 
# El parametro = a la cant de CARACTERES que quiero leer
linea = archivo_sin_leer.readline()
print(linea)

#cerrar el archivo 
archivo_sin_leer.close()
#si no lo cerramos podemos perder datos o cambios. Cerrar desp de usar siempre


