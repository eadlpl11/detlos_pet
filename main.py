import functions

salir = True
functions.clear()

while salir == True:
    print("Bienvenido a la base de datos detlos")

    print("Seleccione una operación:")
    print("1.- Consultar información")
    print("2.- Registrar cliente, mascota o servicio")
    print("3.- Crear respaldo")
    print("4.- Salir")
        
    salir = functions.leer()    