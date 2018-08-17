# Semaphore and mutex
# look up candy.py in threads for semaphores in github

# creating your own thread

import threading

class SubThread(threading.Thread):
    def run(self):
        print("Running...\n")
        return

for i in range(5):
    t = SubThread()
    print("Running thread ",i)
    t.start()
    t.join()
