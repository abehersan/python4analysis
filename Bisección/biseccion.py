f = lambda x: x**2 - 16
a = 10
b = 2
tol = 0.0001
maxitr = 10

def biseccion (f, a, b, tol, maxitr):
    i = 1
    FA = f(a)
    while (i <= maxitr):
        p = a + (b-a)/2
        FP = f(p)
        if (FP == 0) or ((b-a)<tol):
            print ("la raíz es aproximadamente = ", p)
        i += 1
        if ((FA * FP)>0):
            a = p
            FA = FP
        b = p
    print ("el método concluyó después de las iteraciones = ", i)
    
raíz = biseccion (f, a, b, tol, maxitr)