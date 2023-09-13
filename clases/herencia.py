class vehiculo:
    def __init__(self, patente, anio, color):
        self.patente = patente
        self.anio = anio
        self.color = color
    
    def antiguedad(self):
        return f"El vehiculo es del {self.anio}"

class auto(vehiculo):
    def __init__(self,patente,anio,color):
        super().__init__(patente, anio, color) #super()es la funcion que te permite acceder a los metodos y atributos de la clase padre

auto1 = auto("AF253FD", 2022, "Rojo")
antiguedad1 = auto1.antiguedad()
print(antiguedad1)
print(auto1.anio , auto1.patente)



