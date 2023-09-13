#reescribir  el archivo
with open('archivos\\texto.txt','w', encoding="UTF-8") as archivo:
    #reescribir  el archivo
    #archivo.write("Escribiendo el archivo desde python")
    archivo.writelines(["Hola aca no sobreescribo nada\n","Otra linea\n", "Linea 3"])





