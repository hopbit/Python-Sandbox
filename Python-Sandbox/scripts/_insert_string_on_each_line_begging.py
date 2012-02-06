import os
inputFile="input.txt" # in current directory
outputFile="output.txt"
character="'";
if os.path.isdir(inputFile) == False:
    f = open(inputFile,'r')
    o = open(outputFile,'w')
    for line in f:
        line = character+line
        o.write(line)
    o.close()
    f.close()
