import math
f = lambda x: #funcion de x
a = #limite inferior de integracion
b = #limite superior
n = #particiones, siempre PAR

def simpson(f, a, b, n):
    h = (b-a)/n
    XI0 = f(a) - f(b)
    XI1 = 0
    XI2 = 0
    for i in range(1,n):
        X = a + i*h
        if i % 2==0:
            XI2 = XI2 + f(X)
        else:
            XI1 = XI1 + f(X)
    XI = h*(XI0 + 2*XI2 + 4*XI1)/3
    return XI

print("el valor de la integral de","funcion de x",\
      "evaluada desde", a,"a",b,"es", \
      simpson(f,a,b,n), "al dividir el intervalo en", \
      n, "particiones")
    