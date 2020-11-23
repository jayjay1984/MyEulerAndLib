# higly divisible triangular number
DEBUG = False

import problem_3
import problem_5
import math

def first_highly_divisible_triangular2():
    """calculates and returns the first triangular number which has 'factors' divisors
    """

    tria_num = 1

    for i in range(2,20000):
        tria_num += i
        tria_num_sig = problem_5.prime_signature(tria_num)
        num_divisor = 1
        for k in tria_num_sig:
            num_divisor *= (tria_num_sig[k]+1)

        #print(tria_num)
        #print(tria_num_sig)
        if(num_divisor > 400):
            print(tria_num)
            print(num_divisor)
        elif(i % 1000 == 0):
            print(f"i = {i}")


def first_highly_divisible_triangular(factors):
    """calculates and returns the first triangular number which has 'factors' divisors

    Args:
        factors (integer): number of factors
    """

    prime_grid = problem_3.prime_grid(factors)

    divisor_count = []

    tria_num = 1

    

    for i in range(2,100):
        tria_num += i
        k = 0
        divisors = [1, tria_num] #tria_num is always dividable by 1 and itself
        divident = tria_num
        while ((k<len(prime_grid) and (prime_grid[k] <= math.floor(math.sqrt(tria_num))))):
            if(divident % prime_grid[k] == 0):
                divisors.append(prime_grid[k])
                divident /= prime_grid[k]
            else:
                k += 1
        if(divident != 1):
            divisors.append(divident)

        print(tria_num)
        print(divisors)

        divisor_count.append(len(divisors))
    
    print(max(divisor_count))
        



if __name__ == "__main__":

    first_highly_divisible_triangular2()







