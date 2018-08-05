import re
import io
import shutil
import os
import sys

def remove_comments(file1, file2):
    """
    This function removes comments from a file. Comments are considered to be
    lines that start with a #
    
    Arguments:
        file1 {file} -- Actual file to work on
        file2 {file} -- Temporary file where the result is stored
    """

    if file1 != "" and file1 is not None:
        pt = re.compile("#.*")
        file1 = os.path.dirname(os.path.realpath(__file__))+"\\"+file1
        with open(file1, "r+") as fp:
            with open(file2,"w") as fp_2:
                while True:
                    line = fp.readline()
                    if line == '':
                        break
                    line = pt.sub("", line)
                    fp_2.write(line)
        shutil.copy(file2, file1)
        os.remove(file2)


def main():
    remove_comments("example.txt","temp.txt")


if __name__ == "__main__":
    main()
