import os

for filename in os.listdir('.'):
	if os.path.isdir(filename) == False:
		old = filename
		new = old.lower()
		# or upper()
		os.rename(old,new)