def coefficients(a,b,c):
    return lambda x: a*x**2 + b*x + c


def main():
    a = coefficients(1, 2, 3)
    b = map(a, [1, 2, 3])
    for y in b:
        print(y)
    
    
if __name__ == "__main__":
    main()