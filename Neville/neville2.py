datosx = [1.0, 1.3, 1.6, 1.9, 2.2]
datosfx = [0.7651977, 0.6200860, 0.45544022, 0.2818186, 0.1103623]
x = 1.5

import numpy as np
def neville(datosx, datosfx, x):
    m = len(datosx)
    A = np.zeros((m,m))  #:forma representativa en tabla
    A[:, 0] = np.array (np.array (datosfx)) #array imaginario llenado progresivamente
    for k in range (1, m):
        for i in range (m-k):
            A[i, k]= format(round(((x-datosx[i+1]) * A[i, k-1] + \
             (datosx[i]-x) * A[i+1, k-1]) \
             / (datosx[i]-datosx[i+1]), 7))
            #algoritmo de iteracion y redondeo a 7 cifras
    return A #polinomios iterados

print(neville(datosx, datosfx, x))