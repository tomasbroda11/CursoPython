#funcion saludar
def saludar():
    print("Hola  como andas?")

#ejecutando saludar
saludar()

#funcion saludar con parametros
def saludando(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = ""
    
    print(f"Hola {nombre} {adjetivo}, como andas?")

nombre = input("Ingrese su nombre")
sexo = input("Ingrese su sexo")
saludando(nombre , sexo)


 































