from Datos import Datos
class GestionDatos:
    def __init__(self):
        self._lista=[]
    
    @property
    def lista(self):
        return self.l_ista
    
    @lista.setter
    def lista(self,lista):
        self._lista=lista
        
    def agregar_datos(self,datos:Datos)->Datos:
        self._lista.append(datos)
        
    def ConsultarDatos(self,cedula)->Datos:
        for datos in self.lista:
            if datos.cedula==cedula:
                return datos
            
