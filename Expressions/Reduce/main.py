# reduce function reduces a range to a single value depending upon the conditions
import functools


def multiply(x, y):
    return x * y

 
def main():
    # this conducts factorial of 9
    print(functools.reduce(multiply, range(1,10)))

    # using lambda
    print(functools.reduce(lambda x, y: x*y, range(1,10)))


if __name__ == "__main__":
    main()