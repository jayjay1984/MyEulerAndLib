# Largest palindrome product
DEBUG = False

def dec_digit_list(digit_list):
    digit_list[-1] -= 1
    i = -1
    while((digit_list[i] < 0) and (len(digit_list)+i > 0)):
        digit_list[i-1] -= 1
        digit_list[i] = 9
        i -= 1


def palindrom_generator(digits):
    middle = digits // 2 + digits % 2
    digit_list = [9]*(middle)


    while(sum(digit_list)>0):  
        print(digit_list)

        for i in digit_list:
            print(i, end='')
        
        if(digits % 2 == 0):
            for k in digit_list[::-1]:
                print(k, end='')
        else:
            for k in digit_list[::-2]:
                print(k, end='')
        print("\n")
        dec_digit_list(digit_list)
        

def check_palindrom(number):
    text_number = str(number)
    return (text_number == text_number[::-1])

def largest_palindrom_prod(digits):
    largest = 0

    upper = 10 ** digits - 1
    lower = 10 ** (digits-1) + 1

    for i in range(upper,lower, -1):
        if(largest>0):
            limit = largest // i
        else:
            limit = lower
        for k in range(upper,limit, -1):
            p = i * k
            if(check_palindrom(p)):
                if(p > largest):
                    largest = p
                    print(f"{p} = {i} * {k}")
            
    
    return (largest)

if __name__ == "__main__":
    print(largest_palindrom_prod(3))



