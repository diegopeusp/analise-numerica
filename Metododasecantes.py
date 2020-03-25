import math
def fx(x):
    fx =math.cos(x)-x # Escrever a função f(x)
    return fx
def metodosecante(p0,p1,TOL,No):
    i = 2
    q0=fx(p0)
    q1=fx(p1)
    print('#iteração\tg(f(x))\t\terror')
    while i <= No:
        p= p1 - ((p1-p0)*q1/(q1-q0))  
        er = abs(p - p1)
        print("%d\t\t%.6f\t\t%.6f"%(i,p,er));
        if er < TOL:
            return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
        i=i+1
        p0=p1
        q0=q1
        p1=p1
        q1=fx(p)
    return "Atingido o número máximo de iteraçoes" +" "+ str(i) 
print(metodosecante(0,math.pi,1e-10,5)) # Exemplo