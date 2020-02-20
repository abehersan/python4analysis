datosx = [1.0, 1.3, 1.6, 1.9, 2.2]
datosfx = [0.7651977, 0.6200860, 0.45544022, 0.2818186, 0.1103623]

import numpy as np
def newtondd(datosx, datosfx):
	n = len(datosx)
	P = np.zeros((n,n))
	for j in range(n):
		P[j,0] = datosfx[j] #llena columnas, forma representativa
	for i in range(1,n):		
		for j in range(n-i):	
			P[j,i] = round((P[j+1,i-1]-P[j,i-1])/\
            (datosx[j+i]-datosx[j]), 7)
            #algoritmo de iteración y redondeo a 7 cifras
	return P

print(newtondd(datosx, datosfx))