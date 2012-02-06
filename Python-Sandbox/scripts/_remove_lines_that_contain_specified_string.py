import os
inputFile="input.txt" # in current directory
outputFile="output.txt"
string="''";
if os.path.isdir(inputFile) == False:
    f = open(inputFile,'r')
    o = open(outputFile,'w')
    for line in f:
        if(line.count(string)<1):
            o.write(line)
    o.close()
    f.close()
