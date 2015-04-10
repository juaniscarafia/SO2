import pickle
from catedra import Bloque

if __name__ == '__main__':

    datos = (
        # (ID, Cantidad de Memoria)
        (1, 3),
        (2, 2),
        (3, 4),
        (4, 1),
        (5, 2),
    )

    l = []
    for d in datos:
        l.append(Bloque(d[0], d[1]))

    p = open('datos.pkl', 'wb')
    pickle.dump(l, p)
    p.close()
