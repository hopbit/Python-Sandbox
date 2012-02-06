import os
prefix_old = "prefix"
sufix = ".html"
for filename in os.listdir('.'):
    if filename.startswith(prefix_old):
        new = filename+sufix
        os.rename(filename,new)