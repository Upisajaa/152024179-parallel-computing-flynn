import numpy as np
import time

print("=== SISD: Single Instruction Single Data ===")

# ukuran matrix
size = 300

# generate matrix
A = np.random.rand(size, size)
B = np.random.rand(size, size)

start_time = time.time()

# proses serial (single processor)
C = np.zeros((size, size))

for i in range(size):
    for j in range(size):
        for k in range(size):
            C[i][j] += A[i][k] * B[k][j]

end_time = time.time()

print("Matrix multiplication completed")
print("Execution Time (SISD):", end_time - start_time, "seconds")