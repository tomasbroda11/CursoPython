#importando modulos de otras carpetas, a travez de rutas
import sys 

#print(sys.builtin_module_names) #esto muestra los modulos ya creados en python

#print(sys.path) #muestra la ruta de los modulos
sys.path.append("C:\Users\tomas\OneDrive\Escritorio\Programar\Python\funciones")

import misFunciones 
salud = saludando("Tomas","hombre")
print(salud)

#no funciona esto 


