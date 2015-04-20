# -*- coding: utf-8 -*-
import pickle
from catedra import Bloque, Algoritmo, Memoria, SOException


class PrimerAjuste(Algoritmo):

    def __init__(self):
        super(PrimerAjuste, self).__init__("PrimerAjuste")

    def colocar(self, dato):
        bandera = False
        libre = False
        global ultimo
        if not self.memoria.datos and self.memoria.longitud >= dato.tamanio:
            #si la lista está vacía, se carga el primer dato en la posicion cero
            dato.inicio = 0
            dato_fin = dato.tamanio - 1
            ultimo = dato_fin
        else:
            #sino, se recorre la memoria buscando el primer bloque en el que sea posible
            #guardar el dato
            for pos in self.memoria.datos:
                if bandera == False:
                    if pos.id_proceso == None:
                        libre = True
                        #se calcula el tamanio real del bloque
                        tamanio = pos.tamanio - pos.inicio + 1
                        if tamanio >= dato.tamanio:
                            dato.inicio = pos.inicio
                            dato_fin = pos.tamanio
                            indice = self.memoria.datos.index(pos)
                            #se elimina la posicion de la lista para evitar repeticiones
                            #de bloques
                            del self.memoria.datos[indice]
                            bandera = True
            if bandera == False:
                #si no hay ningun bloque disponible para guardar, se opta por optimizar antes de
                #crear un bloque nuevo
                if libre == True:
                    #si existen bloques vacios se optimiza
                    self.memoria.combinar()
                    self.memoria.compactar()
                    #se vuelve a recorrer la lista, buscando un bloque para colocar el dato
                    for pos in self.memoria.datos:
                        if bandera == False:
                            if pos.id_proceso == None:
                                tamanio = pos.tamanio - pos.inicio + 1
                                if tamanio >= dato.tamanio:
                                    dato.inicio = pos.inicio
                                    dato_fin = pos.tamanio
                                    indice = self.memoria.datos.index(pos)
                                    del self.memoria.datos[indice]
                                    bandera = True
                if bandera == False:
                    #si trata de optimizar, y aun asi no puede colocar el dato, o si no hay
                    #ningun bloque vacio, y no es posible optimizar, se crea uno nuevo en caso
                    #de que haya memoria suficiente
                    if memoria.longitud >= dato.tamanio:                  
                        dato.inicio = ultimo + 1
                        dato_fin = (dato.inicio + (dato.tamanio - 1))
                        ultimo = dato_fin
                        bandera = True
                    else:
                        #si no hay espacio en la memoria, se larga una excepcion
                        raise SOException("Memoria insuficiente")


class MejorAjuste(Algoritmo):

    def __init__(self):
        super(MejorAjuste, self).__init__("MejorAjuste")

    def colocar (self, dato):
        optimo = False
        bandera = False
        libre = False
        global ultimo
        if not self.memoria.datos and self.memoria.longitud >= dato.tamanio:
            #si la lista está vacía, se carga el primer dato en la posicion cero
            dato.inicio = 0
            dato_fin = dato.tamanio - 1
            ultimo = dato_fin
        else:
            mejor = 1000
            for pos in self.memoria.datos:
                #se recorre la memoria buscando el bloque que genere menor desperdicio
                if optimo == False:
                    #tamanio real del bloque
                    tamanio = pos.tamanio - pos.inicio + 1
                    if pos.id_proceso == None:
                        libre = True
                        if tamanio >= dato.tamanio:
                            if tamanio == dato.tamanio:
                                #si se encuentra un bloque que no genere nada de desperdicio
                                #se detiene la búsqueda
                                mejor = pos.tamanio
                                posicion = pos
                                optimo = True
                            elif mejor > tamanio:
                                mejor = pos.tamanio
                                posicion = pos
                                bandera = True
            if optimo == True or bandera == True:
                #si se encuentra alguna posicion de memoria disponible para el dato, este se guarda
                dato.inicio = posicion.inicio
                dato_fin = posicion.tamanio
                indice = self.memoria.datos.index(posicion)
                #se elimina la posicion de la lista para evitar repeticiones
                #de bloques
                del self.memoria.datos[indice]
            else:
                #si no hay bloques disponibles, se intenta optimizar
                optimo = False
                bandera = False
                if libre == True:
                    #si existen bloques vacios se optimiza
                    self.memoria.combinar()
                    self.memoria.compactar()
                    mejor = 1000
                    for pos in self.memoria.datos:
                        #vuelve a recorrerse la memoria
                        if optimo == False:
                            tamanio = pos.tamanio - pos.inicio + 1
                            if pos.id_proceso == None and tamanio >= dato.tamanio:
                                if tamanio == dato.tamanio:
                                    mejor = pos.tamanio
                                    posicion = pos
                                    optimo = True
                                elif mejor > tamanio:
                                    mejor = pos.tamanio
                                    posicion = pos
                                    bandera = True
                    if optimo == True or bandera == True:
                        #nuevamente, si se encuentra lugar, se guarda el dato
                        dato.inicio = posicion.inicio
                        dato_fin = posicion.tamanio
                        indice = self.memoria.datos.index(posicion)
                        del self.memoria.datos[indice]
                if bandera == False and optimo == False:
                    #si trata de optimizar, y aun asi no puede colocar el dato, o si no hay
                    #ningun bloque vacio, y no es posible optimizar, se crea uno nuevo en caso
                    #de que haya memoria suficiente
                    if memoria.longitud >= (ultimo + dato.tamanio):
                        dato.inicio = ultimo + 1
                        dato_fin = (dato.inicio + (dato.tamanio - 1))
                        ultimo = dato_fin
                        bandera = True
                    else:
                        #si no hay espacio en la memoria, se larga una excepcion
                        raise SOException("Memoria insuficiente")



class PeorAjuste(Algoritmo):

    def __init__(self):
        super(PeorAjuste, self).__init__("PeorAjuste")

    def colocar(self, dato):
        """Colocacion de bloques en memoria"""
        raise NotImplementedError


class MemoriaAlumno(Memoria):

    def combinar(self):
        #se calcula el numero de bloques para evitar exceder el rango de la lista
        numero_bloques = len(self.datos) 
        #se ordena la lista en forma ascendente por inicio
        self.datos = sorted(self.datos, key=lambda datos: datos.inicio)
        for pos in self.datos[:]:
            #se recorre la lista ya ordenada de inicio a fin, buscando bloques vacios adyacentes
            actual = self.datos.index(pos)
            siguiente = actual + 1
            if siguiente < numero_bloques:
                if self.datos[actual].id_proceso == None and self.datos[siguiente].id_proceso == None:
                    #se actualizan los valores de uno de los bloques, y se elimina el otro
                    self.datos[siguiente].inicio = self.datos[actual].inicio
                    self.datos[siguiente].tamanio = self.datos[actual].tamanio + self.datos[siguiente].tamanio
                    del self.datos[actual]
                    #como hay una eliminacion, se calcula nuevamente el numero de bloques
                    numero_bloques = len(self.datos)

    def compactar(self):
        #se calcula el numero de bloques para evitar exceder el rango de la lista
        numero_bloques = len(self.datos)
        #se ordena la lista en forma ascendente por inicio
        self.datos = sorted(self.datos, key=lambda datos: datos.inicio)
        for pos in self.datos[:]:
            #se recorre la lista ya ordenada, de inicio a fin, buscando bloques vacios separados
            #por bloques ocupados
            actual = self.datos.index(pos)
            siguiente = actual + 1
            if siguiente < numero_bloques:
                if self.datos[actual].id_proceso == None and not self.datos[siguiente].id_proceso == None:
                    #se hace el corrimiento de datos, para que el bloque ocupado quede en primer lugar (antes
                    #que el vacio)
                    tamanio = self.datos[siguiente].tamanio - self.datos[siguiente].inicio + 1
                    self.datos[siguiente].inicio = self.datos[actual].inicio
                    self.datos[siguiente].tamanio = (self.datos[siguiente].inicio + (tamanio - 1))
                    tamanio = self.datos[actual].tamanio - self.datos[actual].inicio + 1
                    self.datos[actual].inicio = self.datos[siguiente].tamanio + 1
                    self.datos[actual].tamanio = (self.datos[actual].inicio + (tamanio - 1))
        #se llama a la funcion combinar para acomodar los bloques vacios ahora adyacentes
        self.combinar()


if __name__ == '__main__':

    for algoritmo in [PrimerAjuste(), MejorAjuste()]:
        #, PeorAjuste()
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
            memoria.combinar()
            # Compactar
            # memoria.compactar()
        except NotImplementedError:
            print "El algoritmo no esta implementado"