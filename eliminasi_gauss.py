print("Nama : Masdar")
print("NIM : H061181022")

print("Latihan 4.1")
print("Eliminasi Gauss dengan Metode Pivoting")

from numpy import array,zeros,fabs, linalg

A = array ([[0, 2, 0, 1],
            [2, 2, 3, 2],
            [4, -3, 0, 1],
            [6, 1, -6, -5]], float)
b = array ([0, -2, -7, 6], float)

print("Solutition of Numpy")
print(linalg.solve(A,b))

n = len(b);
x = zeros(n,float);

#Elimination
for k in range(n-1):
    if fabs(A[k,k]) < 1.0e-12:
        for i in range(k+1,n):
            if fabs (A[i,k]) > fabs(A[k,k]):
                A[[k,i]] = A[[i,k]]
                b[[k,i]] = b[[i,k]]
                break
    for i in range(k+1,n):
        if A[i,k] == 0:continue
        factor = A[k,k]/A[i,k]
        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j]*factor
        b[i] = b[k] - b[i]*factor
print(A)
print(b)

#Back-subtitution
x[n-1] = b[n-1] / A[n-1, n-1]
for i in range (n-2, -1, -1):
    sum_Ax = 0
    for j in range(i+1,n):
        sum_Ax += A[i,j] * x[j]
    x[i] = (b[i] - sum_Ax) / A[i,i]
    
print('The solution of the system:')
print('Nilai x0, x1, x2, x3:')
print(x)