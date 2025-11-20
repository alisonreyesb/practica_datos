#importacion de las clases
from Datos import Datos
from GestionDatos import GestionDatos
print("MENU DE LISTA")
#instanciacion de las clases
gt=GestionDatos()
dt=Datos()
lista=[]
#creacion del bucle para el menu
while True:
#opciones para el menu    
    print("1. Agregar")
    print("2. Consultar")
    print("3. Salir")
    print("4. Mostrar Lista")
#espacio para escribir la opcion q se desea utilizar
    opcion=int(input("Ingrese la opcion q desea utilizar: " ))
#opcion numero uno nos permite agrega los datos de la persona a la lista
    if opcion==1:
        print("Ingrese los datos de la persona")
        dt.nombre=str(input("Ingrese el nombre de la persona: "))
        dt.apellido=str(input("Ingrese el apellido: "))
        dt.edad=int(input("Ingrese la edad: "))
        dt.correo=str(input("Ingrese el correo: "))
        dt.cedula=int(input("Ingrese el numero de cedula: "))
        gt.agregar_datos(dt)
#opcion numero dos nos permite consultar un elemento de la lista con el numero de la cedula
    elif opcion==2:
        cedula=int(input("Ingrese el numero de cedula que  desea consultar:  "))
        gt.ConsultarDato(cedula)
        print(gt.ConsultarDatos(cedula))
#opcion 3 nos permite salir del programa
    elif opcion==3:
        print("Saliendo del programa")
        break