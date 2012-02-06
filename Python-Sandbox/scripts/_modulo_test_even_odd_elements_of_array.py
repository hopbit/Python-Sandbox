import os
inputFile="input.txt" # in current directory
outputFile="output.txt"
a="["
b=","
c="],"
if os.path.isdir(inputFile) == False:
    f = open(inputFile,'r')
    o = open(outputFile,'w')
    i = 0
    for line in f:
        if i%2==0:
            line=a+line.replace("\n",(b+"\n"))
        if i%2==1:
            line=line.replace("\n",(c+"\n"))
        o.write(line)
        i=i+1
    o.close()
    f.close()
