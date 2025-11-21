#importacion de las clases necesarias
from Datos import Datos
from typing import List
#Definicion de la clase GestionDatos
class GestionDatos:
    def __init__(self):
        self._lista =[]
    
    @property
    def lista(self)->List:
        return self._lista

    @lista.setter
    def lista(self, lista:List):
        self._lista=lista

#Metodo para agregar datos a la lista
    def agregar_datos(self, datos:Datos):
        self.lista.append(datos)

#Metodo para consultar datos por cedula
    def consultarDatos(self, cedula:int)->Datos:
        for datos in self.lista:
            if datos.cedula == cedula:
                return datos
