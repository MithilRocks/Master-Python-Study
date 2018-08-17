import threading
import time
from collections import namedtuple


def worker(name, lname):
    # time.sleep(3)
    print(name, lname)
    print(threading.currentThread().getName())


def main():
    Point = namedtuple('Point', ['name', 'lname'])
    t = threading.Thread(target=worker, args=Point("Mithil","Bhoras"), name = ("Worker Thread"))
    t.start()
    # if t.join isn't given, the print in worker will come at the third second
    t.join()
    for i in range(5):
        time.sleep(1)
        print(i)
    
    
if __name__ == "__main__":
    main()