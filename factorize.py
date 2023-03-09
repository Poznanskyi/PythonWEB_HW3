from time import time
from multiprocessing import cpu_count, Pool


def factorize(*args: list):
    result = []
    for num in args:
        res = []
        for i in range(1, num+1):
            if num % i == 0:
                res.append(i)
        result.append(res)
    return tuple(result)


if __name__ == "__main__":
    data = [128, 255, 99999, 10651060]
    start = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f"Normal {time() - start}")
    start_pool_process = time()
    with Pool(cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, data)
        pool.close()
        pool.join()
    print(f"Pool {time() - start_pool_process}")
