#importacion de las clases necesarias
from Datos import Datos 
from GestionDatos import GestionDatos
#Creacion del objeto de GestionDatos
gd=GestionDatos()
#Menu para interactuar con el usuario
menuActivo=True
while menuActivo:
    #Se realiza un menu para verifica las funciones
    print("No Registros: ", len(gd.lista))
    print("-----------------")
    print("Menu de opciones")
    print("1. Agregar")
    print("2. Consultar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")
    #Se solicita que ingrese la opcion que va a elegir
    opcion=input("Ingrese una opcion: ")

    if opcion == "1":
        dt=Datos()
        dt.nombre = str(input("Ingrese su nombre: "))
        dt.apellido = str(input("Ingrese su apellido: "))
        dt.cedula = int(input("Ingrese su numero de cedula: "))
        dt.correo = str(input("Ingrese su correo: "))
        dt.edad = int(input("Ingrese su edad: "))
        gd.agregar_datos(dt)
    
    elif opcion == "2":
        cedula = int(input("Ingrese numero de cedula para la Consulta: "))
        result=gd.consultarDatos(cedula)
        if(result!=None):
            print("Nombre completo:",result.nombre,result.apellido, "Edad:",result.edad, "Correo electronico:",result.correo, "Identificaion:",result.cedula)
    
    elif opcion == "3":
        #funcion para modificar los datos
        cedula = int(input("Ingrese numero de cedula para Modificar: "))
        dt=Datos()
        dt.nombre = str(input("Ingrese su nombre: "))
        dt.apellido = str(input("Ingrese su apellido: "))
        dt.cedula = int(input("Ingrese su numero de cedula: "))
        dt.correo = str(input("Ingrese su correo: "))
        dt.edad = int(input("Ingrese su edad: "))
        gd.modificarDatos(cedula,dt)
    
    elif opcion == "4":
        #funcion para eliminar los datos
        cedula = int(input("Ingrese numero de cedula para Eliminar: "))
        gd.eliminarDatos(cedula)
        
    elif opcion == "5":
        #Con esta opcion se sale del programa
        print("Saliendo del programa")
        break