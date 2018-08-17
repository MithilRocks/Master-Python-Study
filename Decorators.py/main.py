import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        print("Function started: ", time.time())
        func()
        print("Function ended: ", time.time())
    return wrapper

@time_taken
def foo():
    print("In Foo")
    for i in range(1,1000000):
        pass

foo()
