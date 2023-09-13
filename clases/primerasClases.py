class persona:
    def __init__(self,nombre,apellido,edad,direccion,mail ):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.mail = mail
    
#    def __str__(self): #sirve para que una cadena represente a nuestro objeto
   #     return f"{self.nombre} {self.apellido} tiene {self.edad} años"

    #defino metodo para persona
    def saludar(self):
        print(f"Hola {self.nombre}, como va tu dia?")

    
pers1 = persona("Tomas","Broda","22", "Entre rios 1339", "tomasbroda13@gmail.com")
print(pers1.nombre , pers1.apellido)

pers1.saludar()

        


