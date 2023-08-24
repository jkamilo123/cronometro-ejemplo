from unidadtiempo import UnidadTiempo

class Segundo(UnidadTiempo):
    def __init__(self):
        self.valor = 0
        self.tope = 60 

if __name__ =='__main__':
    u = Segundo ()
   
    cont = 0
    while cont < 120:
        print(u.valor)
        u.avanzar()
        cont += 1