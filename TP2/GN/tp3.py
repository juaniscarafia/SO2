# -*- coding: utf-8 -*-
from catedra import Algoritmo


class Optimo(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(Optimo, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError


class LRU(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(LRU, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError


class FIFO(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(FIFO, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError


class Reloj(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(Reloj, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError
