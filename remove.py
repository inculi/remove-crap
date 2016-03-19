import os
import sys

def removeCrap():
    if sys.argv[1] == "*":
        for file in os.listdir(os.curdir):
            for x in range(2, len(sys.argv)):
                filename = file
                if "*" in sys.argv[x]:
                    if sys.argv[x][0] in file and sys.argv[x][len(sys.argv[x]) - 1] in file:
                        toremove = filename.rsplit(sys.argv[x][0])[1].rsplit(sys.argv[x][len(sys.argv[x]) - 1])[0]
                        toremove = sys.argv[x][0] + toremove + sys.argv[x][len(sys.argv[x]) - 1]
                        filename = filename.replace(toremove, "")
                elif sys.argv[x] in file:
                    filename = file.replace(sys.argv[x], "")
                os.rename(file, filename)
    else:
        filename = sys.argv[1]
        for x in range(2, len(sys.argv)):
            if "*" in sys.argv[x]:
                print sys.argv[x]
            else:
                filename = filename.replace(sys.argv[x], "")
        os.rename(sys.argv[1], filename)

if len(sys.argv) > 1:
    removeCrap()
else:
    print "Not enough arguments. Command structure is as follows:"
    print "First argument: file name, or * for all files"
    print "Second argument: String to remove, or to remove all characters in parenthesis, do (*)"
    print "remove.py can take an infinite number of arguments, but give arguments in the order they are in the filename"
