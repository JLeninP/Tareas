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
    
#-----------------------------------------
#PROGRAMA
if __name__ == '__main__':
    archivo: object = open("datos.in", "r")

    n: int = int(archivo.readline())

    A: list[list[float]] = []
    for i in range(n):
        A.append(list(map(float, archivo.readline().split())))

    b: list[float] = list(map(float, archivo.readline().split()))

    X0 = [0 for i in range(n)]

    TOL: float = float(archivo.readline())

    N: int = int(archivo.readline())

    
    sys.stdout.write(f'\nMatriz: {n}x{n}\n')

    sys.stdout.write(f'\nVector A:\n')
    for elem in A:
        sys.stdout.write(f'{elem}\n')

    sys.stdout.write(f'\nVector b: {b}\n')

    sys.stdout.write(f'\nVector X0: {X0}\n')
    
    sys.stdout.write(f'\nTolerancia: {TOL}\n')

    sys.stdout.write(f'\nNúmero Máximo de Iteraciones: {N}\n')


    SOLUCION: list[float] = Gauss_Siedel(n, A, b, X0, TOL, N)

    sys.stdout.write(f'\nSOLUCIÓN:')
    sys.stdout.write(f'\nXi = {SOLUCION[0]}')
    sys.stdout.write(f'\nIteraciones = {SOLUCION[1]}')

    
