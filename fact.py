import time
import multiprocessing

def factorize(*numbers):
    result = []
    for num in numbers:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def factorize_mul(*numbers):
    result = []
    with multiprocessing.Pool() as pool:
        result = pool.map(find_factors, numbers)
    return result

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


numbers = (128, 255, 99999, 10651060)

start_time = time.time()
result_sync = factorize(*numbers)
end_time = time.time()
execution_time_sync = end_time - start_time
print("Synchronous version execution time:", execution_time_sync, "seconds")

start_time = time.time()
result_parallel = factorize_mul(*numbers)
end_time = time.time()
execution_time_parallel = end_time - start_time
print("Parallelized version execution time:", execution_time_parallel, "seconds")
