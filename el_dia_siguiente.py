class ciudad:
    def __init__(self,nombre,edificios_ciudad=[]):
        self.nombre = nombre
        self.edificios_ciudad = edificios_ciudad

class empleado:
    def __init__(self,nombre):
        self.nombre = nombre

class empresa:
    def __init__(self,propietario,edificios_empresa=[]):
        self.propietario = propietario
        self.edificios_empresa = edificios_empresa
    def destruir(self):
        print(len(self.edificios_empresa))

class edificio(empresa,ciudad):
    def __init__(self,nombre,empleado):
        self.nombre = nombre
        self.empleado = empleado
    def despedir(self,trabajador):
        if self.empleado.nombre==trabajador:
            self.edificios_empresa=self.edificios_empresa.remove(edificio(self.nombre,self.empleado))
            self.edificios_ciudad=self.edificios_ciudad.remove(edificio(self.nombre,self.empleado))
        else:
            print("holu")











los_angeles=ciudad("los_angeles",[edificio("C",empleado("xing"))])
new_york=ciudad("new_york",[edificio("A",empleado("martin")),edificio("B",empleado("salim"))])
empresa1=empresa("yoohoo",[edificio("A",empleado("martin")),edificio("B",empleado("salim")),edificio("C",empleado("xing"))])
edificio("C",empleado("xing")).despedir("xing")
empresa1.destruir()