---
title: "Asistencia"
subtitle: "Ejemplo 11.3"
author: "Lenin Pocoaca"
date: "17-09-24"
---

# Método Iterativo Gauss-Siedel

```{python, collapse = TRUE, echo = FALSE}

import sys

def sumatoria(a: list[float], X: list[float], i: int, n: int) -> float:
    res: float = 0.0
    for j in range(i, n):
        res += a[j] * X[j]
    
    return res

def tolerancia(X: list[float], X0:list[float], n: int) -> float:
    L = []
    for i in range(n):
        L.append(abs(X[i] - X0[i]))
 
    return max(L)

def Gauss_Siedel(n: int, A: list[list[float]], b: list[float], X0: list[float], TOL: float = 1e-10, N: int = 1000) -> tuple[list[float], int]:
    X: list[float] = X0[:]
    for _ in range(N):
        for i in range(n):
            X[i] = 1/A[i][i] * (-sumatoria(A[i], X, 1, i - 1) - sumatoria(A[i], X0, i + 1, n) + b[i])
        
        if tolerancia(X, X0, n) < TOL: return (X, _ + 1)
        X0 = X[:]
        
    
    else:
        sys.stdout.write("\nNumero de Iteraciones excedido...")
        return (X, _ + 1)
    

# Entrada de datos

n: int = 3

A: list[list[float]] = [
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
]

b: list[float] = [7.85, -19.3, 71.4]

X0 = [0, 0, 0]

TOL: float = 0.001 # Valor por convención

N: int = 20 # Valor por convención
    

SOLUCION: list[float] = Gauss_Siedel(n, A, b, X0, TOL, N)

sys.stdout.write(f'\nSOLUCIÓN:')
sys.stdout.write(f'\nXi = {SOLUCION[0]}')
sys.stdout.write(f'\nIteraciones = {SOLUCION[1]}')
```

## Salida en pantalla
Con Tolerancia de 0.001
```{python, collapse = TRUE, echo = FALSE}
Xi = [3.0109619047619045, -2.451142857142857, 7.140000000000001]
Iteraciones = 4
```
## Referencias
Richard L. Burden (2016). ANÁLISIS NUMÉRICO (10ma ed.). (p. 339).