class edificio:
    def __init__(self,nombre,empleado):
        self.nombre = nombre
        self.empleado = empleado
    def destruir(self,empresa,ciudad):
        if self in empresa.edificios:
            empresa.edificios=empresa.edificios.remove(self)
        else:
            print(f'el {self} no pertenece a la empresa de {empresa.propietario}')
        if self in ciudad.edificios:
            ciudad.edificios=ciudad.edificios.remove(self)
        self.empleado="muerto"
        print(f'edificio {self.nombre} fue destruido')
        if ciudad.edificios==[]:
            print(f'{ciudad.nombre} fue destruida')
        if empresa.edificios==[]:
            print(f'la empresa de {empresa.propietario} desaparecio')


class ciudad:
    def __init__(self,nombre,edificios=list()):
        self.nombre = nombre
        self.edificios = edificios
    def numero_edificios(self):
        print(len(self.edificios))
    def destruir(self,empresa):
        for i in range(len(self.edificios)):
            edificio=self.edificios[i]
            if edificio in empresa.edificios:
                empresa.edificios=empresa.edificios.remove(edificio)
            self.edificios=self.edificios.remove(edificio)
        print(f'{self.nombre} fue destruido')
        if empresa.edificios==[]:
            print(f'la empresa de {empresa.propietario} desaparecio')



   # def __del__(self):
    #    for i in self.edificios:
   #         self.edificios=self.edificios.remove(i)
    #    print(f'La ciudad {self.nombre} fue destruida por una catastrofe')

class empleado:
    def __init__(self,nombre):
        self.nombre = nombre

class empresa:
    def __init__(self,propietario,edificios=list()):
        self.edificios=edificios
        self.propietario = propietario
    def numero_edificios(self):
        print(len(self.edificios))



edificio_c=edificio("C",empleado("xing"))
edificio_a=edificio("A",empleado("martin"))
edificio_b=edificio("B",empleado("salim"))
los_angeles=ciudad("los_angeles",[edificio_c])
new_york=ciudad("new_york",[edificio_a,edificio_b])
empresa1=empresa("yoohoo",[edificio("A",empleado("martin")),edificio("B",empleado("salim")),edificio_c])

edificio_c.destruir(empresa1,los_angeles)
edificio_b.destruir(empresa1,new_york)
new_york.destruir(empresa1)
los_angeles.numero_edificios()

#me da problemas como que nontype object is not suscriptable o iterable y si quito los if compo utilizo remove para eliminar elementos de la lista
#si hay algun elemento que no esta en la lista me lanza la excepcion de x not in list
#no se como arreglar esos problemas