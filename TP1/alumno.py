import pickle
from catedra import Bloque, Algoritmo, Memoria, SOException


class PrimerAjuste(Algoritmo):

    def __init__(self):
        super(PrimerAjuste, self).__init__("PrimerAjuste")

    def colocar(self, dato):
        # """Colocacion de bloques en memoria"""
        # raise NotImplementedError
        FinMayor = 0
        mem_insuficiente = 0
        if self.memoria.datos == []:
            if self.memoria.longitud >= dato.tamanio:
                dato.inicio = 0
                dato_fin = dato.tamanio - 1
            else:
                print "MEMORIA INSUFICIENTE"
        else:
            corte = False
            while dato.inicio == None and corte == False:
                c = 0       
                for x in self.memoria.datos:
                    c = c + 1
                    if x.id_proceso == None and dato.tamanio <= x.tamanio and dato.inicio == None:
                        dato.inicio = x.inicio 
                        dato_fin = dato.inicio + dato.tamanio - 1
                        if dato.tamanio < x.tamanio:
                            x.inicio = dato_fin + 1
                            x.tamanio = x.tamanio - dato.tamanio
                        else:
                            del self.memoria.datos[ c - 1 ]
                     
                if dato.inicio == None:
                    Bandera = 0
                    for x in self.memoria.datos:
                        if Bandera == 0:
                            FinMayor = x.tamanio - 1
                            Bandera = 1
                        else:
                            if FinMayor < x.tamanio - 1:
                                FinMayor = x.tamanio -1
                    if self.memoria.longitud - FinMayor + 1 > dato.tamanio:
                        dato.inicio = FinMayor + 1
                        dato_fin = dato.inicio + dato.tamanio - 1
                    # else:
                    #     if mem_insuf == 0:
                    #         memoria.compactar()
                    #         print "Intento de Compactar"
                    #     if mem_insuf == 1:
                    #         memoria.combinar()
                    #         print "Intento de Combinar"
                    #     if mem_insuf ==2:
                    #         print "MEMORIA INSUFICIENTE"
                    #         corte = True
                    #     mem_insuf=mem_insuf+1


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
