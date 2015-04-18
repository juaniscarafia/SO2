# -*- coding: utf-8 -*-
"""
Clases utilizadas en los trabajos prácticos de la cátedra SO II en la UCSE DAR.
"""


class SOException(Exception):
    """Excepción base para los errores reportados por los algoritmos.
    Todos los controles que no deben permitir continuar con la ejecución
    normal de los procesos, se deben terminar con una SOException."""

    def __init__(self, msg):
        self.msg = unicode(msg)

    def __unicode__(self):
        return unicode(self.msg)

    def __str__(self):
        return self.msg


class Bloque(object):
    """Estructura que representa un bloque a colocar en memoria. Debe estar
    asociado a un proceso e indicar el tamaño requerido. En el atributo
    "inicio" posee la dirección base de memoria en el caso de encontrarse en
    memoria, sino es None (indicando que el proceso aún no se colocó)."""

    def __init__(self, id_proceso, tamanio):
        self.id_proceso = id_proceso
        self.tamanio = tamanio
        self.inicio = None

    def __repr__(self):
        return u"<Bloque | proceso: {0}, memoria: {1} (+{2})>".format(
            self.id_proceso, self.inicio, self.tamanio)


class Algoritmo(object):
    """Clase base para realizar los algoritmos de colocacion."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.memoria = None

    def __repr__(self):
        codmem = "" if self.memoria is None else self.memoria.codigo()
        return u"<Algoritmo | {0}, memoria: {1}>".format(self.nombre, codmem)

    def colocar(self, dato):
        """Logica para ubicar el bloque en la posición correcta según el
        algoritmo seleccionado."""
        raise NotImplementedError


class Memoria(object):
    """Clase que representa la memoria"""

    def __init__(self, longitud, nombre='RAM'):
        self.longitud = longitud
        self.datos = []
        self.valores = " " * longitud
        self.algoritmo = None
        self.nombre = nombre

    def __repr__(self):
        return "<Memoria | {0} {1}>".format(self.valores, self.longitud)

    def ocupado(self):
        return self.longitud - sum([b.tamanio for b in self.datos])

    def codigo(self):
        return u"{0} ({1}/{2})".format(self.nombre, self.ocupado(),
                                       self.longitud)

    def usar(self, algoritmo):
        """Asigna el algoritmo que utilizara la memoria para colocar los nuevos
        bloques en la memoria"""
        if self.algoritmo is not None:
            self.algoritmo.memoria = None  # Desafecto el algoritmo actual
        self.algoritmo = algoritmo
        self.algoritmo.memoria = self

    def colocar(self, bloque):
        """Coloca un bloque en la memoria segun el algoritmo asociado"""
        try:
            # El algoritmo me tiene que devolver el inicio para el bloque
            self.algoritmo.colocar(bloque)
            if bloque.inicio is None:
                raise SOException(
                    "{0} no ha especificado inicio o fin para el bloque de "
                    "memoria.".format(self.algoritmo))
            else:
                self.datos.append(bloque)
                self.valores = (
                    self.valores[:bloque.inicio] +
                    str(bloque.id_proceso)[0] * bloque.tamanio +
                    self.valores[bloque.inicio + bloque.tamanio:]
                )
        except SOException, e:
            print "<ERROR: %s>" % e

    def liberar(self, bloque):
        """Libera el bloque de moria especificado"""
        if bloque.inicio is None or bloque.id_proceso is None:
            print SOException("El bloque indicado no se encuentra en memoria.")
        else:
            self.valores = (
                self.valores[:bloque.inicio] + " " * bloque.tamanio +
                self.valores[bloque.inicio + bloque.tamanio:]
            )
            bloque.id_proceso = None

    def combinar(self):
        """Combinar bloques adyasentes"""
        raise NotImplementedError

    def compactar(self):
        """Compactar bloques (defragmentar)"""
        raise NotImplementedError
