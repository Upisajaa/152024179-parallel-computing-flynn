import multiprocessing
import numpy as np
import time

print("=== Parallel Matrix Multiplication (MIMD) ===")

# ukuran matrix
size = 300

# generate matrix random
A = np.random.rand(size, size)
B = np.random.rand(size, size)

# fungsi untuk setiap process
def multiply_row(args):
    row, B = args
    return np.dot(row, B)

if __name__ == "__main__":

    start_time = time.time()

    # menjalankan parallel process
    with multiprocessing.Pool() as pool:
        result = pool.map(
            multiply_row,
            [(A[i], B) for i in range(size)]
        )

    end_time = time.time()

    print("Matrix multiplication completed")
    print("Execution Time:", end_time - start_time, "seconds")