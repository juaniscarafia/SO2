# -*- coding: utf-8 -*-
from copy import copy


class Marco(object):

    def __init__(self):
        self.valor = None
        self.bit = False
        self.apuntado = False

    def __repr__(self):
        ptr = ">" if self.apuntado else " "
        bit = "*" if self.bit else " "
        valor = " " if self.valor is None else self.valor
        return "|%s%02d%s|" % (ptr, valor, bit)


class Algoritmo(object):

    def __init__(self, cantidad_marcos):
        self.nombre = self.__class__.__name__
        self.marcos = []
        self.historia = []
        self.llamadas = []
        for i in range(cantidad_marcos):
            self.marcos.append(Marco())
        self.marcos[0].apuntado = True

    def __repr__(self):
        return "<Algoritmo '%s'>" % self.nombre

    def visualizar_historia(self):
        if len(self.historia) > 0:
            for l in range(len(self.historia[0])):
                for m in self.historia + [self.marcos, ]:
                    print m[l],
                print ""
            print "-" * 80

    def colocar(self, pagina, paginas=None):
        if paginas is None:
            raise Exception(u"Se requiere la lista completa de páginas")
        if len(self.marcos) == 0:
            raise Exception(
                u"No se han inicializado los marcos de págian disponibles")
        self.historia.append([copy(i) for i in self.marcos])
        self.llamadas.append(pagina)
