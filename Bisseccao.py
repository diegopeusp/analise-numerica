import math
def f(x):
    f =math.cos(x)-x # Escrever a função f(x)
    return f    
def metodobiseccion(a,b,TOL,No):
    if f(a)*f(b) < 0:
        i = 1
        fa=f(a)
        print('#iteração\tP_i\t\terror')
        while i <= No:
            p=(a+b)/2
            fp=f(p)
            er =(b-a)/2
            print("%d\t\t%.6f\t\t%.6f"%(i,p,er));
            if er < TOL or fp == 0:
                return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
            i=i+1
            if (fa*fp)>0:
                a=p
                fa=fp
            else:
                b=p
        return "Atingido o número máximo de iteraçoes" +" "+ str(i) 
    else:
        print("No existe raiz en este intervalo")
print(metodobiseccion(-1,2,1e-5,1000))