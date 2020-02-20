import math as math
import numpy as np
from prettytable import PrettyTable

f = lambda t,y: y - t**2 + 1 #derivadas de orden superior y(n)(t,y)
g = lambda t: (t+1)**2 - (0.5)*math.exp(t) #primitiva y(t)
a = 0 #límite inferior
b = 2 #límite superior
n = 10 #particiones siempre PAR
p = 0.5 #condición inicial y(a)=p

def taylor(f,a,b,n,p):
    h = (b-a)/n
    t = a
    w = p
    lista_a = [a]
    lista_b = [p]
    lista_c = [g(a)]
    lista_d = [p-g(a)] #listas para ti, wi, yi y error
    
    for i in range(1,n+1):
        t = round(a + i * h, 2) #calcula ti
        evaly = round(g(t), 7) #calcula yi
        for j in range(n):
            q = round(a + j * h)
            w = round(1.22*w - 0.0088*q**2 - 0.008*q + 0.22,7)
            err = round(abs(evaly - w), 7)
            lista_b.append(w)
            lista_c.append(evaly)
            break
        #w = round(w + h*((1 + h/2)*(w - q**2 + 1) - h*q), 7) #calcula wi
        #err = round(abs(evaly - w), 7)
        lista_a.append(t)
        lista_d.append(err) #añade los valores a las listas
    
    t = PrettyTable()
    
    nombres = ['ti','wi','err']
    
    t.add_column(nombres[0], lista_a)
    t.add_column(nombres[1], lista_b)
    #t.add_column(nombres[2], lista_c)
    t.add_column(nombres[2], lista_d)
    
    print(t)
    
    return 'listo profe Puch'

print (taylor(f,a,b,n,p))
        