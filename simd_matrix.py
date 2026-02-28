import numpy as np
import time

print("=== SIMD: Single Instruction Multiple Data ===")

# ukuran matrix
size = 300

# generate matrix
A = np.random.rand(size, size)
B = np.random.rand(size, size)

start_time = time.time()

# single instruction untuk banyak data
C = np.dot(A, B)

end_time = time.time()

print("Matrix multiplication completed")
print("Execution Time (SIMD):", end_time - start_time, "seconds")