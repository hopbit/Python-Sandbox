import os
postfix='_1.JPG'
for filename in os.listdir('.'):
	if os.path.isdir(filename) == False:
		if filename.endswith(postfix):
			os.remove(filename)
