import math as math
import numpy as np
from prettytable import PrettyTable

f = lambda t,y: y - t**2 + 1 #derivada y'(t,y)
g = lambda t: (t+1)**2 - (0.5)*math.exp(t) #primitiva y(t)
a = 0 #límite inferior
b = 2 #límite superior
n = 10 #particiones siempre PAR
p = 0.5 #condición inicial y(a)=p

def euler(f,a,b,n,p):
    h = (b-a)/n
    t = a
    w = p
    lista_a = [0.0]
    lista_b = [0.5]
    lista_c = [0.5]
    lista_d = [0.0] #listas para ti, wi, yi y error
    
    for i in range(1,n+1):
        w = round(w + h * f(t,w), 7) #calcula wi
        t = round(a + i * h, 2) #calcula ti
        evaly = round(g(t), 7) #calcula yi
        err = round(abs(evaly - w), 7)
        lista_a.append(t)
        lista_b.append(w)
        lista_c.append(evaly)
        lista_d.append(err) #añade los valores a las listas
    
    t = PrettyTable()
    
    nombres = ['ti','wi','yi','err']
    
    t.add_column(nombres[0], lista_a)
    t.add_column(nombres[1], lista_b)
    t.add_column(nombres[2], lista_c)
    t.add_column(nombres[3], lista_d)
    
    print(t)
    
    return 'listo profe Puch'

print (euler(f,a,b,n,p))
        