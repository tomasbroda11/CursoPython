                                #la diferencia esta en la 'a'
with open('archivos\\texto.txt','a', encoding="UTF-8") as archivo:
    #agregando el archivo
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")





