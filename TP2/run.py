# -*- coding: utf-8 -*-
from GN import Optimo, LRU, FIFO, Reloj


class Prueba(object):

    def __init__(self, marcos, paginas):
        self.marcos = marcos  # Cantida de marcos a utilizar
        self.paginas = paginas  # Listado de páginas a procesar


def main():
    pruebas = [
        # Conjunto de pruebas obligatorio
        Prueba(3, [1, 2, 5, 3, 8, 5, 4, 2, 8, 3, 7, 1]),
        Prueba(4, [2, 5, 3, 4, 7, 6, 3, 8, 1, 3, 6, 2]),
        # Los alumnos deben agregar mas conjuntos de prueba
    ]

    for prueba in pruebas:
        print "*" * 80
        print u"  Páginas: %s" % prueba.paginas
        for algoritmo in [Optimo, LRU, FIFO, Reloj]:
            try:
                a = algoritmo(prueba.marcos)
                print "\nEjecutando %s" % a
                print "-" * 80
                for p in prueba.paginas:
                    a.colocar(p, prueba.paginas)
                a.visualizar_historia()
            except NotImplementedError:
                print "Algoritmo no implementado"
        print "\n"


if __name__ == '__main__':
    main()
