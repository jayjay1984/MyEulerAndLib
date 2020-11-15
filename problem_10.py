# largest prime factor
DEBUG = False

import problem_3
import time

def sum_of_primes(limit):
    """calculate and return the sum of all primes smaller than limit.
    """
    s = 0
    pg = problem_3.prime_grid(limit)
    
    #print(pg)
    for p in pg:
        s += p
        
    return s

def prime_sieve(limit):
    sieve = list(range(2,limit))

    #print(sieve)
    i = 0

    while (i<len(sieve)):
        non_prime = 2 * sieve[i]
        while(non_prime < limit):
            #print(f"try to remove {non_prime}")
            try:
                sieve.remove(non_prime)
            except:
                pass

            non_prime = non_prime + sieve[i]
        i += 1

    return sieve

def sum_of_primes2(limit):
    """calculate and return the sum of all primes smaller than limit.
    """
    s = 0
    pg = prime_sieve(limit)
    
    #print(pg)
    for p in pg:
        s += p
        
    return s


if __name__ == "__main__":
    t0 = time.time()
    print(sum_of_primes(100000))
    t1 = time.time()

    print(f"this took {t1-t0}")

    t0 = time.time()
    ps = sum_of_primes2(20000)
    t1 = time.time()

    print(f"prime sieve took {t1-t0}")






