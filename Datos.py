
class Datos:
    def __init__(self):
        pass
    
    @property
    def nombre(self)->str:
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre:str):
        self._nombre=nombre
        
        
    @property
    def apellido(self)->str:
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido:str):
        self._apellido=apellido
        
    @property
    def edad(self)->int:
        return self._edad
    
    @edad.setter
    def edad (self,edad:int):
        self._edad=edad
        
    @property
    def correo(self)->str:
        return self._correo
    
    @edad.setter
    def correo(self,correo:int):
        self._correo=correo
        
    @property
    def cedula(self)->int:
        return self._cedula
    
    @cedula.setter
    def cedula(self,cedula:int):
        self._cedula=cedula