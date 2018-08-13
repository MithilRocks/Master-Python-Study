class AutoGenerate:
    """Simulates range function using generator
    
    Raises:
        StopIteration -- Raised when range is exceeded
    
    Returns:
        int -- integer incremented using step
    """

    
    def __init__(self, start, end, step = 1):
        self.start = start
        self.end = end
        self.step = step

    
    def Next(self):
        self.start += self.step
        if self.start >= self.end:
            raise StopIteration
        yield self.start


    # for 2.7 
    def next(self):
        return self.Next().next()


    # for 3.x
    def __next__(self):
        return self.Next().__next__()


    def __iter__(self):
        return self


def main():
    x = AutoGenerate(0, 100, 5)
    print(next(x))    
    
    
if __name__ == "__main__":
    main()