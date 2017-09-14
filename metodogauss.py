
import math   
import numpy as np

def troca(A,Ep,Ej):
    listaAux = A[Ep].copy()  
    A[Ep] = A[Ej]
    A[Ej] = listaAux
    
def argmax(A,k):
  for j in range(len(A)):
    if(j == 0):
      min = A[j][j]
      ind = j
    if(min > abs(A[j][j])):
      ind = j
      min = A[j][j]
  if(min != 0):
    return j
  return ind
    
def backward(A):
    n, m = np.shape( A )
    #Deixo minha matriz triangular
    for i in range(len(A)):
        p = argmax(A,i)
        if(not type(p) is int):
           print("no unique solution exists")
           return
        if(p != i):
            troca(A,p,i)
        for j in range(i + 1,n):
          m = A[j][i]/A[i][i]
          A[j][i] = A[j][i] - m*A[i][i]
          #Para as outras colunas também tenho que multiplicar, se o lado esquerdo é diferente de 0 
          for k in range(0 ,len(A) + 1):
            if(A[j][k] != 0):
              A[j][k] = A[j][k] -m * A[i][k]
        if(A[n - 1][n - 1] == 0 ): # Pois começa no 0
          print("no unique solution exists")
          return
    #Aqui é minha solução temporária
    Xn = A[n - 1][n]/A[i][i]
    #Aqui faço a técnica de substituição
    X = []
    X.append(Xn)
    for i in range(len(A) - 2, -1, -1):
      j = i + 1
      temp = 0
      for k in range(len(X) - 1,-1,-1):
        temp = temp + A[i][j]*X[k]
        j = j + 1
      temp = (A[i][n] - temp)/A[i][i]
      X.append(temp)

    return X



print(backward(np.array([[1,-1,3,2],
                     [3,-3,1,-1],
                     [1,1,2,3],
                     ])))

                     
