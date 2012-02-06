import os
old_prefix='_some_prefix'
new_prefix='some_new_prefix'
for filename in os.listdir('.'):
	if os.path.isdir(filename) == False:
		if filename.startswith(old_prefix):
			old = filename
			new = new_prefix+filename.replace(old_prefix,'')
			os.rename(old,new)