# largest prime factor
DEBUG = False

import problem_3

def sum_of_primes(limit):
    """calculate and return the sum of all primes smaller than limit.
    """
    s = 0
    pg = problem_3.prime_grid(limit)
    
    #print(pg)
    for p in pg:
        s += p
    
    return s
    

if __name__ == "__main__":
    print(sum_of_primes(100000))





