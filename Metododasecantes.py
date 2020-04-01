import math
def fx(x):
    fx = math.atan(x)-2*x+1 # Escrever a função f(x)
    return fx
def metodosecante(p0,p1,TOL,No):
    i = 1
    q0=fx(p0)
    q1=fx(p1)
    print('#iteração\tg(f(x))\t\terror')
    while i <= No:
        p= p1 - ((p0-p1)*q1/(q0-q1))  
        er = abs(p - p1)
        print("%d\t\t%.6f\t\t%.6f"%(i,p,er));
        if er < TOL:
            return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
        i=i+1
        p0=p1
        q0=q1
        p1=p
        q1=fx(p)
    return "Atingido o número máximo de iteraçoes" +" "+ str(i) 
print(metodosecante(0,1,1e-8,100)) # Exemplo