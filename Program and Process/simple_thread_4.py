import threading
import time

data = 0
lock = threading.Lock()

def global_data():
    global data
    lock.acquire()
    data += 1
    time.sleep(0.1)
    x = data
    lock.release()
    return x


def process_job():
    print(global_data())


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=process_job)
        threads.append(t)
        t.start()
        t.join()

    for x in threads:
        x.join()
        
    
if __name__ == "__main__":
    main()