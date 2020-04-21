import math
def descompositiontridiagonal(A,B):
    n = len(A)
    D= [0  for i in range(n)]
    L= [0 for i in range(n-1)]
    D[0]=A[0]
    for i in range(1,n):
        L[i-1]=B[i-1]/D[i-1]          
        D[i]=A[i]-(L[i-1]**2)*D[i-1]
    return L,D
# QX=b ---> (LDLT)X=b.   Q is symmetric tridiagonal
def fwdSubstitution(L,b):   #Forward substitution,solves the equation LZ=b
    n = len(b)
    Z = [0 for i in range(n)]
    Z[0] = b[0]
    for i in range(1,n):
        Z[i] = b[i] - Z[i-1]*L[i-1]
    return Z  

def diagonalSubstitution(D,Z):   #Diagonal substitution,solves the equation DY=Z
    n = len(D)
    Y = [0 for i in range(n)]
    for i in range(n):
        Y[i]=Z[i]/D[i]    
    return Y

def backSubstitution(L,Y):  #Backwards substitution,solves LTX=Y, returns the solution of LTX=Y
    n = len(Y)
    X = [0 for i in range(n)]
    X[n-1] = Y[n-1]
    for i in range(n-2,-1,-1):
        X[i] = Y[i]-X[i+1]*L[i]
    return X

def tridiagonalsystemsolution(A,B,b):
    L , D = descompositiontridiagonal(A,B)
    Z = fwdSubstitution(L,b)
    Y = diagonalSubstitution(D,Z)
    X = backSubstitution(L,Y)
    print ("X=",X)
# Exemplo
A=[2, 2, 2, 2, 2]   #diagonal vetor of Q size n.
B=[1, 1, 1 ,1]      #Subdiagonal vetor OF Q size n-1.
b=[1, 1, 1, 1,1]   #vetor answer b size  n.
tridiagonalsystemsolution(A,B,b)
