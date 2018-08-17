import threading
import time
# check video on GIL by David Beazely

def foo():
    print("Hello World")
    # sleep won't happen if t.join() isn't given.
    time.sleep(2)


def main():
    t = threading.Thread(target=foo)
    t.start()
    # every process is a thread. The above is a sub-thread to this program (thread)
    # by giving t.join(), main will wait till the thread isn't complete.
    # if join is not there, it'll directly go ahead to the next line without waiting
    # essentially we are "joining" threads so that they don't have random serialization
    t.join()
    print("Main going further")


if __name__ == "__main__":
    main()