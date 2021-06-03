import os

def readFromFile(filename):
    if os.path.exists(filename):
    # return first line
        f = open(filename, "r")
        line = f.readline()
        return line
    else:
        raise Exception("Bad File")
