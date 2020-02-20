datosx = [1.0, 1.3, 1.6, 1.9, 2.2]
datosfx = [0.7651977, 0.6200860, 0.45544022, 0.2818186, 0.1103623]
x = 1.5

import numpy as np
def neville(datosx, datosfx, x):
    m = len(datosx)
    P = np.zeros((m,m))  #:forma representativa en tabla
    P[:, 0] = np.array (np.array (datosfx)) #array imaginario llenado progresivo
    for i in range (1, m):
        for j in range (m-i):
            P[j, i]= format(round(((x-datosx[j+1]) * P[j, i-1] + \
             (datosx[j]-x) * P[j+1, i-1]) \
             / (datosx[j]-datosx[j+1]), 7))
            #algoritmo de iteracion y redondeo a 7 cifras
    return P #polinomios iterados

print(neville(datosx, datosfx, x))