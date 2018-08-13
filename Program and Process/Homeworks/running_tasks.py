import time
import subprocess

def show_tasks():
    """
    HW: Write a python script which runs periodically and displays the status of currently running processes
    """
    while True:
        print("All running processes: ")
        subprocess.call("tasklist", shell=True)
        time.sleep(5)

def main():
    show_tasks()

if __name__ == "__main__":
    main()