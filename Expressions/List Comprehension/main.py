# make one line lists
def list_comprehension(lb = 2, ub = 10):
    return [x * x for x in range(lb, ub + 1) if x % 2 == 0]


# wap to generate a list of multiples of 3 and 5 from the given range
def multiple_of_three_and_five(lb=1, ub = 100):
    return [x for x in range(lb, ub + 1) if x % 15 == 0]


# wap to generate a pair from the given two list of unique elements in them
def unique_pair(range1 = range(1,4), range2 = range(2,5)):
    return [ (x, y) for x in range1 for y in range2 if x != y]


def main():
    print(multiple_of_three_and_five())


if __name__ == "__main__":
    main()