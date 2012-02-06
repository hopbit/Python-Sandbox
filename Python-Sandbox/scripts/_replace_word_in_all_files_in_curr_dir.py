# this script read all files in current 
# directory line by line, replace each 
# occurence of old_word with new_word 
# and write it to new file
# TODO 	1. drop all old files 
#	2. smash ___NEW___ prefix in all 
#	   newly created files
import os
old_word='old word to replace'
new_word='new word to replace'
for filename in os.listdir('.'):
	if os.path.isdir(filename) == False:
		f = open(filename)
		o = open('___NEW___'+filename,'a')
		for line in open(filename):
			line = line.replace(old_word,new_word)
			o.write(line)
		o.close()
		f.close()
