"""class interfaz_cristal:
  def __init__(self,ventanas=[],paredcortina=[]):
    self.ventanas=ventanas
    self.paredcortina=paredcortina
  def superficie(self):
    list=[]
    i=0
    j=0
    for i in range(0,len(self.ventanas)):
      list.append(self.ventanas[i].superficie)
    for j in range(0,len(self.paredcortina)):
      list.append(self.paredcortina[j].superficie)
    return sum(list)"""

class interfaz_cristal2:
  def __init__(self,cristal,superficie):
    self.cristal = cristal
    self.superficie=superficie


class ParedCortina:
  def __init__(self,orientacion):
    self.orientacion = orientacion
    #self.superficie = superficie


class Pared:
    
  def __init__(self, orientacion,):
    self.orientacion = orientacion



class Ventana:

  def __init__(self, objeto_pared, proteccion):
    self.orientacion = objeto_pared.orientacion
    #self.superficie = superficie
    self.proteccion = proteccion
    
    if(proteccion!="Persiana" and proteccion!="Estor"):
      raise Exception("Protección obligatoria ")

class Casa:

  def __init__(self, norte, oeste, sur, este):
    self.norte = norte.superficie
    self.oeste = oeste.superficie
    self.sur = sur.superficie
    self.este = este.superficie


  def superficie_acristalada(self):
    return (self.norte + self.oeste + self.sur + self.este)
    





pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = ParedCortina("SUR") 
pared_este = Pared("ESTE") 


ventana_norte = Ventana(pared_norte,"Persiana") 
ventana_oeste = Ventana(pared_oeste,"Persiana") 
ventana_este = Ventana(pared_este,"Persiana") 


"""casa = Casa(ventana_norte, ventana_oeste, pared_sur, ventana_este) 
print(casa.superficie_acristalada()) 

cristal=interfaz_cristal([ventana_norte,ventana_oeste,ventana_este],[pared_sur])
print(cristal.superficie())"""

casa2=Casa(interfaz_cristal2(ventana_norte,2),interfaz_cristal2(ventana_este,3),interfaz_cristal2(ventana_oeste,2),interfaz_cristal2(pared_sur,2))
print(casa2.superficie_acristalada())