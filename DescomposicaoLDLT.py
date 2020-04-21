import math
def descompositiontridiagonal(A,B):
    n = len(A)
    D= [0  for i in range(n)]
    L= [0 for i in range(n-1)]
    D[0]=A[0]
    for i in range(1,n):
        L[i-1]=B[i-1]/D[i-1]          
        D[i]=A[i]-(L[i-1]**2)*D[i-1]
    print("L=",L)
    print("D=",D)
# QX=b ---> (LDLT)X=b.   Q is symmetric tridiagonal
# Exemplo
A=[2, 2, 2, 2, 2]   #diagonal vetor of Q size n.
B=[1, 1, 1 ,1]      #Subdiagonal vetor of Q size n-1.
descompositiontridiagonal(A,B)