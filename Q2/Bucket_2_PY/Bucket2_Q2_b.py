import numpy as np
import time

def matrix_multiply(N,dtype):
    A = np.ones((N,N), dtype=dtype)
    B = np.ones((N,N), dtype=dtype)
    C = np.zeros((N,N), dtype=dtype)

    start = time.time()

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = A[i][k]*B[k][j]

    end = time.time()
    meat = end - start

    return meat



n = int(input("Enter the Matrix Dimension Value (N): "))

#integer
print("Integer :")
start_int = time.time()
meat_int = matrix_multiply(n, np.int32)
end_int = time.time()
total_int = end_int-start_int
print(f"Time Taken for Meat Portion : {meat_int:.6f} seconds")
print(f"Total Time : {total_int:.6f} seconds")
print(f"Proportion of Meat Portion w.r.t Total Time: {meat_int / total_int:.2%}")


print("\n")


#double
print("double:")
start_double = time.time()
meat_double = matrix_multiply(n, np.float64)
end_double = time.time()
total_double = end_double-start_double
print(f"Time Taken for Meat Portion: {meat_double:.6f} seconds")
print(f"Total Time : {total_double:.6f} seconds")
print(f"Proportion of Meat Portion w.r.t Total Time: {meat_double / total_double:.2%}")