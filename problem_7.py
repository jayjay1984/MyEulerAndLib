# n-th prime
DEBUG = False

import problem_3

def find_n_th_prime(n):
    primes = problem_3.prime_grid(15*n)
    return primes[n-1]

if __name__ == "__main__":
    print(find_n_th_prime(10001))
    



