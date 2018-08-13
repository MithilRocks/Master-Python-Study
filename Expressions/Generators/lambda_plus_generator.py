def increase(n):
    while True:
        y = lambda x:n+x
        yield y

def main():
    x = increase(6)
    y = next(x)
    print(y(10))
    
    
if __name__ == "__main__":
    main()