# Largest palindrome product
DEBUG = False

import problem_3

def prime_signature(number):
    """calculates and returns a dictionary containing the prime factors of number as key and the numer of occurances as value.

    Args:
        number (integer): number for which the signature shall be calculated
    """
    prime_factors = problem_3.prime_factors(number)

    sig = dict()

    for p in prime_factors:
        if p in sig:
            sig[p] += 1
        else:
            sig[p] = 1
    
    return sig

def smallest_multiple(Limit):
    """calculates and returns the smallest multiple of all numbers below limit

    Args:
        Limit (integer): largest divisor of the result
    """

    smallest_multiple_sig = dict()

    for i in range(2,Limit+1):
        i_sig = prime_signature(i)
        for prim_fac in i_sig:
            if prim_fac in smallest_multiple_sig:
                smallest_multiple_sig[prim_fac] = max(smallest_multiple_sig[prim_fac], i_sig[prim_fac])
            else:
                smallest_multiple_sig[prim_fac] = i_sig[prim_fac]
    
    result = 1

    print(smallest_multiple_sig)

    for prim_fac in smallest_multiple_sig:
        result *= (prim_fac ** smallest_multiple_sig[prim_fac])

    return result

if __name__ == "__main__":
    

    print(smallest_multiple(100))


    



