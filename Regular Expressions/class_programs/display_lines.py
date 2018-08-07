import re

def display_lines(pattern, file):
    """Displays lines containing the pattern
    
    Arguments:
        pattern {string} -- Regex
        file {string} -- The File name
    """

    if file !="" and file is not None:
        pt = re.compile(pattern, flags=2)
        fp = open(file)

        while True:
            line = fp.readline()
            if line == '':
                break
            if pt.search(line):
                print(line)


def main():
    display_lines("[0-9]", "example.txt")


if __name__ == "__main__":
    main()