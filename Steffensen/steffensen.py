def f(x):
    y=x**2 - 16
    return y
p0 = 7
tol = 0.0005
maxitr = 1024

def steff(f, p0, tol, maxitr):
    raices=[]
    for i in range(1,maxitr):
        raices.append(p0)
        p1=p0+f(p0)
        p2=p1+f(p1)
        p=p0-((p1-p0)**2/(p2-2*p1+p0))
        print ((i,p0,p))
        if (abs(p-p0)<tol) :
            print ("la raíz es aproximadamente", p)
            return raices
        p0=p
    print ("el método falló después de las iteraciones =" , i)
    return raices

raiz = steff(f, p0, tol, maxitr)