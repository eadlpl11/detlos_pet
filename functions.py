import datetime
import tkinter
from pymongo import MongoClient
from os import system
from tkinter import filedialog


client = MongoClient(host = 'localhost')
db = client['detlos_pet']

#Colecciones
datos_cliente = db['clientes']
datos_mascota = db['mascotas']
datos_servicio = db['servicios']

clear = lambda: system('clear')

def leer():
    try:
        a = int(input())
        if a == 1:
            consulta()
        if a == 2:
            registro()
        if a == 3:
            respaldo()
        if a == 4:
            return False
        else:
            return True
        if a > 4 or a < 1:
            print("Operación inválida")
            leer()
    except:
        print("Ingrese un número")             
        leer()

def registro():
    
    curp = input("Ingrese CURP: ")
    nombre_cliente = input("Ingrese nombre: ")
    edad_cliente = input("Ingrese edad: ")
    mascota = input("Ingrese nombre de la mascota: ")

    cliente = {
        'curp': curp,
        'nombre': nombre_cliente,
        'edad': edad_cliente,
        'mascota': mascota
    }

    datos_cliente.insert_one(cliente)

    edad_mascota = input("Ingrese la edad de la mascota: ")
    animal = input("Ingrese el tipo de animal: ")

    mascotas = {    
        'nombre': mascota,
        'edad': edad_mascota,
        'animal': animal
    }
    
    datos_mascota.insert_one(mascotas)    

    tipo_servicio = input("Ingrese el tipo de servicio: ")
    monto = int(input("Ingrese el monto: "))

    servicio = {
        'tipo': tipo_servicio,
        'monto': monto,
        'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    datos_servicio.insert_one(servicio)

def consulta():
    clear()
    print("Seleccione una colleción")
    print("1.- Clientes")
    print("2.- Mascotas")
    print("3.- Servicios")

    try:
        a = int(input())
        if a == 1:
            output = datos_cliente.find({})
            for data in output:
                print(data)
        if a == 2:
            output = datos_mascota.find({})
            for data in output:
                print(data)
        if a == 3:
            output = datos_servicio.find({})
            for data in output:
                print(data)
        if a > 4 or a < 1:
            print("Operación inválida")
            consulta()
    except:
        print("Ingrese un número")             
        consulta()

def respaldo():
    direccion = filedialog.askdirectory()
    print('mongodump -d detlos_pet -o ' + direccion + '/respaldo-`date +%Y-%m-%d`')
    system('mongodump -d detlos_pet -o ' + direccion + '/respaldo-`date +%Y-%m-%d`')
    

