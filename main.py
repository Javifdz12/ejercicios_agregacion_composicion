from clases.inmortal import *
from clases.alternativa_herencia_multiple import Pared,Ventana,ParedCortina,interfaz_cristal2,Casa

if __name__ == '__main__':
    print(yang)
    print(yang is yin.yang)
if __name__ == '__main__':
    pared_norte = Pared("NORTE")
    pared_oeste = Pared("OESTE")
    pared_sur = ParedCortina("SUR")
    pared_este = Pared("ESTE")


    ventana_norte = Ventana(pared_norte,"Persiana") 
    ventana_oeste = Ventana(pared_oeste,"Persiana") 
    ventana_este = Ventana(pared_este,"Persiana") 

    casa2=Casa(interfaz_cristal2(ventana_norte,2),interfaz_cristal2(ventana_este,3.5),interfaz_cristal2(ventana_oeste,2),interfaz_cristal2(pared_sur,2))
    print(casa2.superficie_acristalada())

