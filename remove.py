import os
import sys

def removeCrap():
    # Check if user wants to remove crap from all files
    if sys.argv[1] == "-a":
        # Iterate through the arguments
        for x in range(2, len(sys.argv)):
            # Get all files in current directory
            for file in os.listdir(os.curdir):
                filename = file
                # If there is an asterisk in an argument, get the beginning and end of that argument
                if "*" in sys.argv[x]:
                    # Buckle up
                    # Strip the argument and get the first and last characters, and make sure they are both in the filename
                    if sys.argv[x].strip()[0] in file and sys.argv[x].strip()[len(sys.argv[x].strip()) - 1] in file:
                        # Once we make sure they are both in the filename, split the filename by the characters
                        toremove = filename.rsplit(sys.argv[x].strip()[0])[1].rsplit(sys.argv[x].strip()[len(sys.argv[x].strip()) - 1])[0]
                        # Now that we have the portion of the filename that we want to remove, reattach the characters that we split by
                        toremove = sys.argv[x].strip()[0] + toremove + sys.argv[x].strip()[len(sys.argv[x].strip()) - 1]
                        # Remove the text in the filename
                        filename = filename.replace(toremove, "")
                # If there is no asterisk, just remove whatever is in the argument
                elif sys.argv[x] in file:
                    filename = file.replace(sys.argv[x], "")
                os.rename(file, filename)
    else:
        # Check if user wants to remove crap from just one file
        filename = sys.argv[1]
        for x in range(2, len(sys.argv)):
            if "*" in sys.argv[x]:
                if sys.argv[x].strip()[0] in filename and sys.argv[x].strip()[len(sys.argv[x].strip()) - 1] in filename:
                    # Once we make sure they are both in the filename, split the filename by the characters
                    toremove = filename.rsplit(sys.argv[x].strip()[0])[1].rsplit(sys.argv[x].strip()[len(sys.argv[x].strip()) - 1])[0]
                    # Now that we have the portion of the filename that we want to remove, reattach the characters that we split by
                    toremove = sys.argv[x].strip()[0] + toremove + sys.argv[x].strip()[len(sys.argv[x].strip()) - 1]
                    # Remove the text in the filename
                    filename = filename.replace(toremove, "")
            # If there is no asterisk, just remove whatever is in the argument
            elif sys.argv[x] in filename:
                filename = filename.replace(sys.argv[x], "")
        os.rename(sys.argv[1], filename)

if len(sys.argv) > 1:
    removeCrap()
else:
    print "Not enough arguments. Command structure is as follows:"
    print "First argument: file name, or -a for all files"
    print "Second argument: String to remove, or to remove all characters in parenthesis, do (*)"
    print "remove.py can take an infinite number of arguments, but give arguments in the order they are in the filename"
