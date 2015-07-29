# -*- coding: utf-8 -*-
from catedra import Algoritmo


class Optimo(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(Optimo, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError
        # b = 0
        # y = 0
        # w = 0
        # x = 0
        # disponibles = [m for m in self.marcos if m.valor == None]
        # for x in range (len(self.marcos)):
        #     if self.marcos[x].valor == int(pagina):
        #         b = 1
        #         y = x
        # if b == 0:
        #     if len(disponibles) > 0:
        #         m = disponibles[0]
        #     else:
        #         i =len(self.historia) - 1
        #         marco_actual = []
        #         marco_actual_estado = []
        #         for x in range (len(self.marcos)):
        #             marco_actual.append(self.marcos[x].valor)
        #             marco_actual_estado.append(False)
        #         c = 0
        #         x = 0
        #         y = 0
        #         pagina_a_reemplazar = 0
        #         b2 = False
        #         if i + 1 < len(paginas): #si no esta en la ultima
        #             for x in range (i + 1, len(paginas)):#se mueve desde la pagina siguiente a la en uso hasta el final
        #                 for y in range (len(marco_actual)):
        #                     if marco_actual_estado[y] == False and paginas[x] == marco_actual[y]:
        #                         marco_actual_estado[y] = True
        #                         c = c + 1
        #                         if c == len(marco_actual) - 1:
        #                             b2 = True
        #                             for w in range (len(marco_actual)):
        #                                 if marco_actual_estado[w] == False:
        #                                     pagina_a_reemplazar = w
        #             if b2 == False:
        #                 while w < len(marco_actual):
        #                     if marco_actual_estado[w] == False:
        #                         pagina_a_reemplazar = w
        #                         w = len(marco_actual)
        #                     w = w + 1
        #         m = self.marcos[int(pagina_a_reemplazar)]
        #     m.valor = int(pagina)
        #     # m.apuntado = True


class LRU(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(LRU, self).colocar(pagina, paginas)  # Dejar esta línea
        #raise NotImplementedError
        super(LRU, self).colocar(pagina, paginas) # Dejar siempre esta línea
        b = 0
        y = 0
        w = 0
        x = 0
        disponibles = [m for m in self.marcos if m.valor == " "]
        for x in range (len(self.marcos)):
                if self.marcos[x].valor == str(pagina):
                    b = 1
                    y = x

        if b == 0:
            if len(disponibles) > 0:
                m = disponibles[0]
            else:
                i =len(self.historia) - 2
                marco_actual = []
                marco_actual_estado = []
                for x in range (len(self.marcos)):
                    marco_actual.append(self.marcos[x].valor)
                    marco_actual_estado.append(False)
                    #copia el marco (valores) y estado para despues setearlo
                c = 0
                x = i
                y = 0
                pagina_a_reemplazar = 0
                b2 = False
                if i + 1 < len(paginas): #si no esta en la ultima
                    while x > 0:
                    #for x in range (i + 1, len(paginas)):#se mueve desde la pagina siguiente a la en uso hasta el final
                        for y in range (len(marco_actual)):
                            if marco_actual_estado[y] == False and str(paginas[x]) == marco_actual[y]:
                                marco_actual_estado[y] = True
                                c = c + 1
                                if c == len(marco_actual) - 1:
                                    b2 = True
                                    for w in range (len(marco_actual)):
                                        if marco_actual_estado[w] == False:
                                            pagina_a_reemplazar = w
                        x = x - 1

                    if b2 == False:
                        while w < len(marco_actual):
                            if marco_actual_estado[w] == False:
                                pagina_a_reemplazar = w
                                w = len(marco_actual)
                            w = w + 1


                m = self.marcos[pagina_a_reemplazar]
            m.valor = str(pagina)
            #m.apuntado = True


class FIFO(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(FIFO, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError


class Reloj(Algoritmo):

    def colocar(self, pagina, paginas=None):
        super(Reloj, self).colocar(pagina, paginas)  # Dejar esta línea
        raise NotImplementedError
