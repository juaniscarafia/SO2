import pickle
from catedra import Bloque, Algoritmo, Memoria, SOException


class PrimerAjuste(Algoritmo):

    def __init__(self):
        super(PrimerAjuste, self).__init__("PrimerAjuste")

    def colocar(self, dato):
        # """Colocacion de bloques en memoria"""
        # raise NotImplementedError
        bandera = False
        global ultimo
        if not self.memoria.datos and self.memoria.longitud >= dato.tamanio:
            #Si la lista está vacía, se carga el primer dato en la posición cero
            dato.inicio = 0
            ultimo = dato.longitud - 1
        else:
            #Sino, se recorre la memoria buscando el primer bloque en el que sea 
            #posible guardar el dato
            for posicion in self.memoria.datos:
                if bandera == False:
                    if posicion.id_proceso == None:
                        libre = True
                        #Se calcula el tamanio real del bloque
                        tamanio = 


class MejorAjuste(Algoritmo):

    def __init__(self):
        super(MejorAjuste, self).__init__("MejorAjuste")

    def colocar(self, dato):
        """Colocacion de bloques en memoria"""
        raise NotImplementedError


class PeorAjuste(Algoritmo):

    def __init__(self):
        super(PeorAjuste, self).__init__("PeorAjuste")

    def colocar(self, dato):
        """Colocacion de bloques en memoria"""
        raise NotImplementedError


class MemoriaAlumno(Memoria):

    def combinar(self):
        """Combinar bloques adyasentes"""
        raise NotImplementedError

    def compactar(self):
        """Compactar bloques (defragmentar)"""
        raise NotImplementedError


if __name__ == '__main__':

    for algoritmo in [PrimerAjuste(), MejorAjuste(), PeorAjuste()]:
        try:
            print "*" * 80
            print "Ejecutando con: %s" % algoritmo
            print ""

            memoria = MemoriaAlumno(50)
            memoria.usar(algoritmo)

            # Cargar los datos de un archivo
            datos = open('datos.pkl', 'r')
            lista_datos = pickle.load(datos)
            datos.close()

            # Llamar al cargar de la memoria
            print "Cargando los datos generales"
            for dato in lista_datos:
                memoria.colocar(dato)

            # Estado inicial de la memoria
            print "Estado inicial de la memoria"
            print memoria

            # Procesamiento
            if len(memoria.datos) > 0:
                b = memoria.datos[1]
                print "\nLiberar %s" % b
                memoria.liberar(b)
                print memoria
            else:
                print "No hay datos en la memoria para liberar (ERROR)"

            d6 = Bloque(6, 2)
            print "\nColocar %s" % d6
            memoria.colocar(d6)
            print memoria

            print ""
            if len(memoria.datos) > 4:
                for pos in [4, 1, 3]:
                    b = memoria.datos[pos]
                    print "Liberar %s" % b
                    memoria.liberar(b)
                print memoria
            else:
                print "No hay datos suficientes para liberar (ERROR)"

            d7 = Bloque(7, 4)
            print "\nColocar %s" % d7
            memoria.colocar(d7)
            print memoria

            d8 = Bloque(8, 2)
            print "\nColocar %s" % d8
            memoria.colocar(d8)
            print memoria

            d9 = Bloque(9, 10)
            print "\nColocar %s" % d9
            memoria.colocar(d9)
            print memoria

            if len(memoria.datos) > 2:
                b = memoria.datos[-2]
                print "\nLiberar %s" % b
                memoria.liberar(b)
                print memoria
            else:
                print "No hay datos suficientes para liberar (ERROR)"

            d10 = Bloque(0, 2)
            print "\nColocar %s" % d10
            memoria.colocar(d10)
            print memoria

            d11 = Bloque('A', 2)
            print "\nColocar %s" % d11
            memoria.colocar(d11)
            print memoria

            d12 = Bloque('X', 200)
            print "\nColocar %s" % d12
            memoria.colocar(d12)
            print memoria

            d12 = Bloque('Y', 88)
            print "\nColocar %s" % d12
            memoria.colocar(d12)
            print memoria

            d13 = Bloque('Z', 20)
            print "\nColocar %s" % d13
            memoria.colocar(d13)
            print memoria

            # Descomentar las llamadas a las funciones una vez condificadas
            # Combinar
            # memoria.combinar()
            # Compactar
            # memoria.compactar()
        except NotImplementedError:
            print "El algoritmo no esta implementado"
