# Gerade Fibonacci-Zahlen

DEBUG = True

def fibonacci_even_sum(limit):
    """calculates and returns the sum of the even values in the Fibonacci sequence up to limit.

    Args:
        limit ([integer]): [only values up to limit are considered.]
    """

    #init sum
    S = 0

    f0 = 1
    f1 = 1
    if(DEBUG):
        print(f0, end=' ')

    while (f1 < limit):
        h = f1
        f1 = f0 + f1
        f0 = h
        if(f0 % 2 == 0):
            S = S + f0
        if(DEBUG):
            print(f0, end=' ')
    
    if(DEBUG):
        print("\n")

    return S

        

if __name__ == "__main__":
    L = 1000000000
    sum_even_fibo = fibonacci_even_sum(L)

    print(f"the sum of even fibonacci numbers below {L} is {sum_even_fibo}")
