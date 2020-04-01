import math
def f(x):
    f =(x+3)**(1/2) # Escrever a função f(x)
    return f
def ordemeconstante(e0,e1,e2):
  ordem = (math.log(e2/e1))/(math.log(e1/e0))
  constanassi= e2/(e1**ordem)
  print("Ordem de Convergencia é", ordem)
  print("Constante Assintotica é:", constanassi)
  return()
error_i=[]
def puntofijos(p0,TOL,No):
    i = 1
    print('#iteração\tg(f(x))\t\terror')
    while i <= No:
        p= f(p0)  
        er = abs(p - p0)
        error_i.append(er)
        print("%d\t\t%.8f\t\t%.8f"%(i,p,er));
        if er < TOL:
            return "\nA solução mais perta é: %.4f com um error de %.4f"%(p,er)
        i=i+1
        p0=p
    return "Atingido o número máximo de iteraçoes" +" "+ str(i) 
print(puntofijos(1,1e-10,100000)) # Exemplo
ordemeconstante(error_i[1],error_i[2],error_i[3])