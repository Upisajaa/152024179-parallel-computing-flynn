import numpy as np
import time

print("=== MISD: Multiple Instruction Single Data (Simulation) ===")

# ukuran matrix
size = 300

# satu data yang sama
A = np.random.rand(size, size)

# instruksi berbeda pada data sama
def sum_matrix(M):
    return np.sum(M)

def mean_matrix(M):
    return np.mean(M)

def max_matrix(M):
    return np.max(M)

start_time = time.time()

# multiple instruction - single data
s = sum_matrix(A)
m = mean_matrix(A)
mx = max_matrix(A)

end_time = time.time()

print("Sum:", s)
print("Mean:", m)
print("Max:", mx)
print("Execution Time:", end_time - start_time, "seconds")