# Largest palindrome product
DEBUG = False

def sum_of_squares(n):
    S = 0
    for i in range(1,n+1):
        S += i*i
    return S

def square_of_sum(n):
    return ((n)*(n+1)//2)**2

if __name__ == "__main__":
    N = 100

    print(square_of_sum(N) - sum_of_squares(N))


    



