# largest prime factor
DEBUG = False

import math

def prime_grid(limit, grid = []):
    """calculate and return all primes below limit.

    Args:
        limit (integer): limit for the largest prime in the grid.
        grid (list): existing grid which should be extended
    """
    #init empty grid
    if not grid:
        l = [2]
        p = 1
    else:
        l = grid
        p = grid[-1]

    while (p < limit-1):
        p += 2
        skip = False
        for d in l:
            if(d > math.ceil(math.sqrt(p))):
                break
            # check if d divides p
            if((p % d == 0)):
                skip = True
                break
        if(skip):
            continue
        l.append(p)
        if(DEBUG):
            print(p)
    
    return l

def prime_factors(number):
    """calculate and return a set of prime factors

    Args:
        number (integer): number to factorize
    """
    prime_factors = []

    #initial grid
    start_grid = prime_grid(1000)

    for d in start_grid:
        while(number % d == 0):
            prime_factors.append(d)
            number //= d

    #print(number)
    #print(start_grid)

    L = math.floor(math.sqrt(number))
    #print(L)

    good_grid = prime_grid(L, grid=start_grid)
    #print(good_grid)

    for d in good_grid:
        while(number % d == 0):
            prime_factors.append(d)
            number //= d
    
    if(number > 1):
        prime_factors.append(number)

    return prime_factors


if __name__ == "__main__":

    #L = math.floor(math.sqrt(600851475143))
    #print(L)
    #print(prime_grid(L)) -> this takes ages!!!

    pf = prime_factors(600851475143)

    print(pf)

    check = 1

    for f in pf:
        check *= f
    
    print(check)






