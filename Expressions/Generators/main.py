# generators create values on the fly without storing in memory
# the user defined range function using yield

def generator_function(lb = 0, ub = 100, step = 1):
    x = lb
    if step > 0:
        while x < ub:
            yield x
            x += step
    elif step < 0:
        while x > ub:
            yield x
            x += step
    elif step == 0:
        raise ValueError


def main():
    y = generator_function(1, 100, 11)
    print(next(y))


if __name__ == "__main__":
    main()
