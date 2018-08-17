import threading
import time

def worker(num):
    time.sleep(4)
    print(threading.currentThread().getName())
    print("Worker: "+str(num))


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,), name="t"+str(i))
        threads.append(t)
        print("Thread {} starter".format(i))
        t.start()
    
    for x in threads:
        x.join()
    
    
if __name__ == "__main__":
    main()