#todos los archivos .py son modulos 
#importando modulos
import modulo_saludar
saludo = modulo_saludar.saludar(input("Ingresa tu nombre"))
print(saludo)

#operador para asignar 
import modulo_saludar as m_saludar
#otra opcion de importar varias funciones desde un modulo 

from modulo_saludar import saludar, saludar_raro
name = input("Dame tu nombre perrito malvado")
saludo_raro = saludar_raro(name)
print(saludo_raro)
 



