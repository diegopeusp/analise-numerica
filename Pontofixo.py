import math
def f(x):
    f =(x+3)**(1/2) # Escrever a função f(x)
    return f
def puntofijos(p0,TOL,No):
    i = 1
    print('#iteração\tg(f(x))\t\terror')
    while i <= No:
        p= f(p0)  
        er = abs(p - p0)
        print("%d\t\t%.8f\t\t%.8f"%(i,p,er));
        if er < TOL:
            return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
        i=i+1
        p0=p
    return "Atingido o número máximo de iteraçoes" +" "+ str(i) 
print(puntofijos(1,1e-10,100000)) # Exemplo