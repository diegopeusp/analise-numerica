import math

def fx(x):
    fx =math.cos(x)-x # Escrever a função f(x)
    return fx
    
def dfx(x):  
    dfx= -(math.sin(x))-1 # Escrever a derivada f´(x)
    return dfx

def metodonewton(p0,TOL,No):
    i = 1
    print('#iteração\tP_i\t\terror')
    while i <= No:
        p = p0 - (fx(p0) / dfx(p0))
        er = abs(p - p0)
        print("%d\t\t%.6f\t\t%.6f"%(i,p,er));
        if er < TOL:
           return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
        i=i+1
        p0=p
    return "Atingido o número máximo de iteraçoes" +" "+ str(i)
print(metodonewton(math.pi,1e-5,100)) # Exemplo