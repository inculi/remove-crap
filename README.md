# remove-crap
Removes unwanted crap from filenames
# Usage
Command Structure:  
First argument: file name, or * for all files  
Second argument: String to remove, or to remove all characters in parenthesis, do (*)  

remove.py can take an infinite number of arguments, but give arguments in the order they are in the filename  
# Example
File names before remove.py:  
jaykm Episode 1[jaykm uploads 19827].mp4  
jaykm Episode 2[jaykm uploads 62314].mp4  
jaykm Episode 3[jaykm uploads 18070].mp4  
python remove.py * "jaykm " "[*]"  
File names after remove.py:  
Episode 1.mp4  
Episode 2.mp4  
Episode 3.mp4  
