from math import exp, cos, sin, log1p, pi

f = lambda x: x**2 - 16
p0 = 1
p1 = 2
tol = 10e-2
maxitr = 10

def secante (f, p0, p1, tol, maxitr):
    print ("la función es = x**2 - 16") 
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while (i <= maxitr):
        p = p1 - q1*((p1-p0)/(q1-q0))
        if (abs (p-p1) < tol):
            print ("la raíz es aproximadamente = ", p)
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    print ("el método concluyó después de las iteraciones = ", i)
    
raiz = secante (f, p0, p1, tol, maxitr)