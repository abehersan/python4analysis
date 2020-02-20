from math import exp, cos, sin, log1p

f = lambda x: x**2 - 16
df = lambda x: 2*x
p0 = 600
tol = 10e-5
maxitr = 10

def newton (f, df, p0, tol, maxitr):
    print ("la función es = x**2-16") 
    i = 0
    while (i <= maxitr):
        p = p0 - ( f ( p0 ) / df ( p0 ) )
        if abs(p - p0) < tol:
            print ("la raíz es aproximadamente = ", p)
        p0 = p
        i += 1
    print ("el método concluyó después de las iteraciones = ", i)
    
raiz = newton (f, df, p0, tol, maxitr)
