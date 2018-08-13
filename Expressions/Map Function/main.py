def Square(x):
    return x * x


def map_function(range1 = range(1,10)):
    return map(Square, range1)

def map_function_labda(range1 = range(1,10)):
    return map(lambda x: x*x, range1)


def main():
    result = []
    for y in map_function_labda():
        result.append(y)
    print(result)


if __name__ == "__main__":
    main()