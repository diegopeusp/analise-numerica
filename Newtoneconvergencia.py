import math

def fx(x):
    fx =math.tan(x) # Escrever a função f(x)
    return fx
    
def dfx(x):  
    dfx= 1/(math.cos(x)*math.cos(x))# Escrever a derivada f´(x)
    return dfx
def ordemeconstante(e0,e1,e2):
  ordem = (math.log(e2/e1))/(math.log(e1/e0))
  constanassi= e2/(e1**ordem)
  print("Ordem de Convergencia é", ordem)
  print("Constante Assintotica é:", constanassi)
  return()
error_i=[]
def metodonewton(p0,TOL,No):
    i = 1
    print('#iteração\tP_i\t\terror')
    while i <= No:
        p = p0 - (fx(p0) / dfx(p0))
        er = abs(p - p0)
        error_i.append(er)
        print("%d\t\t%.6f\t\t%.6f"%(i,p,er));
        if er < TOL:
           return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
        i=i+1
        p0=p
    return "Atingido o número máximo de iteraçoes" +" "+ str(i)
print(metodonewton(1,1e-8,100)) # Exemplo
ordemeconstante(error_i[1],error_i[2],error_i[3])