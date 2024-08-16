import numpy as np
import time

def matrix_multiply(N,dtype):
    A = np.ones((N,N), dtype=dtype)
    B = np.ones((N,N), dtype=dtype)
    C = np.zeros((N,N), dtype=dtype)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = A[i][k] * B[k][j]



n = int(input("Enter the Matrix Dimension Value (N): "))


#integer
start_int = time.time()
print("Matrix Multiplication for Integer type:")
matrix_multiply(n, np.int32)
end_int = time.time()
total_int = (end_int - start_int)
print(f"Time Taken : {total_int:.6f} seconds\n")


#double
start_double = time.time()
print("Matrix Multiplication for Double type:")
matrix_multiply(n, np.float64)
end_double = time.time()
total_double = (end_double - start_double)
print(f"Time Taken : {total_double:.6f} seconds")
