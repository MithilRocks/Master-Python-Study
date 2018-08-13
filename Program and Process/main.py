"""
A program is a set of instructions
A process is a running instance of a program. It has a life.
A program can last indefinitely

A program file has a PRIMARY HEADER, TEXT REGION, DATA REGION and INFORMATION ABOUT STACK
There is a process table that creates a u-area which contains UFDT.
Also study: per process region table and region table

Python has Global Interpreter Lock. It uses GIL to serialize multi-threaded program which makes
it slower to non-multi threaded programming.

There is a module called subprocess that can spawn a subprocess
"""

import subprocess

# runs the dir command and lists all the directories
# shell = True is for Windows OS to specify shell commands
print(subprocess.call("dir", shell = True))

# will create a new directory
# print("Create new directory", subprocess.call("mkdir exampledir", shell = True))
# this returns 0 for success

# Checks the call for the command and raises exception. Call doesn't

try:
    print(subprocess.check_call("copy", shell = True))
except subprocess.CalledProcessError as er:
    print(er)

# it gives the output of the command and throws CalledProcessError exception otherwise
out = subprocess.check_output("dir", shell = True)
print(out)

# The process is executed on the pipe
c = subprocess.Popen("dir", shell = True, stdout=subprocess.PIPE)

# this gives the output of the command. Calling this again will give 
# an valueerror as the object is destroyed
print(c.communicate())

try:
    print(c.communicate())
except ValueError as er:
    print(er)

# outputs dir result to dir.txt
d = subprocess.Popen("dir", shell=True, stdout=open("dir.txt", "w"))

# study preexec_fn. It works only in Linux. :(
# HW: explore psutil