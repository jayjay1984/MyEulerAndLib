# Vielfache von 3 und 5 
import timeit
import time


def stupid_bruteforce(M, l):
    """[takes list of numbers and summarizes all their multiples below M.]

    Args:
        M ([integer]): [maximum boundary. Multiples are only considerred below]
        l ([List]): [list of number which multiples are considerred]
    """
    #init sum to 0
    S = 0 

    for number in l:
        #e.g. 1000//3 = 333 -> // is floor division
        for i in range(1,(M-1)//number+1):
            #print(f"S: {S} , i: {i} , n: {number}")
            S += i*number

    return S

def stupid_bruteforce_2(M, l):
    """[takes list of numbers and summarizes all their multiples below M.]

    Args:
        M ([integer]): [maximum boundary. Multiples are only considerred below]
        l ([List]): [list of number which multiples are considerred]
    """
    #init sum to 0
    S = 0 

    for i in range(M):
        next = False
        for number in l:
            if(i % number == 0):
                S += i
                next = True
                break
        if(next):
            continue


    return S


def smart_analytical(M, l):
    """[takes list of numbers and summarizes all their multiples below M.]

    Args:
        M ([integer]): [maximum boundary. Multiples are only considerred below]
        l ([List]): [list of number which multiples are considerred]
    """
    #init sum to 0
    S = 0 

    for number in l:
        n = ((M-1)//number)
        S += n*(n+1)/2*number

    return S



if __name__ == "__main__":
    N = 1000
    t0 = time.time()
    print(stupid_bruteforce(N, [3,5]))
    t1 = time.time()
    print(stupid_bruteforce(N, [3,5]))
    t2 = time.time()
    print(stupid_bruteforce_2(N, [3,5]))
    t3 = time.time()

    print(f"stupid took {t1-t0:.6f}")
    print(f"smart took  {t2-t1:.6f}")
    print(f"stupid but correct took {t3-t2:.6f}")


    # measure runtime
    # print(timeit.timeit("stupid_bruteforce(1000, [3,5])",number=1, setup="from __main__ import stupid_bruteforce"))