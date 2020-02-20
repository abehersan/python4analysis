def f(x):
    y=x-2
    return y
p0 = 1
tol = 0.0005
maxitr = 15

def pfijo(f, p0, tol, maxitr):
    raices=[]
    for i in range(1,maxitr):
        raices.append(p0)
        p=f(p0)
        print ((i,p0,p))
        if (abs(p-p0)<tol) :
            print ("la raíz es aproximadamente", p)
            return raices
        p0=p
    print ("el método falló después de las iteraciones =" , i)
    return raices

raiz = pfijo(f, p0, tol, maxitr)