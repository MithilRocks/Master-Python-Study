def notdivisibleby(x):
    return x % 2 != 0 and x % 3 != 0


def filter_out(range1 = range(1,100)):
    return filter(notdivisibleby, range1)


def filter_out_lamda(range1 = range(1,100)):
    return filter(lambda x: x % 2 !=0 and x % 3 !=0, range1)


def main():
    result = []
    for y in filter_out_lamda():
        result.append(y)
    print(result)


if __name__ == "__main__":
    main()