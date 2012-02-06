import os

f = open('lista_plikow.txt','a')

for root, dirs, files in os.walk('./'):
    for name in files:       
        filename = os.path.join(root, name)
        print filename
        f.write(filename+'\n')
f.close()