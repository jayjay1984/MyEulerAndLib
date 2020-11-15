# special pythagorean tripple
DEBUG = False

if __name__ == "__main__":
    S = 8888
    for a in range(1,S-2+1):
        for b in range(a+1,S-a-1+1):
            c = S - a - b
            if((a*a+b*b) == c*c):
                print(f"we have found the special tripple {a} {b} {c} and their product is {a*b*c}")




