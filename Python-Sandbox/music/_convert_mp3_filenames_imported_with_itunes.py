# coding=UTF-8
import os, shutil

cwd = os.getcwd() 

for artistDir in os.listdir('.'): 
	if os.path.isdir(artistDir) == True: 
		artistPath = os.path.join(cwd, artistDir)
		os.chdir(artistPath) 
		for albumDir in os.listdir('.'): 
			albumPath = os.path.join(artistPath,albumDir) 
			os.chdir(albumPath) 
			for fileName in os.listdir('.'): 
				if os.path.isdir(fileName)==False: 
					cdNumber = "" 
					titleStartMarker = 3 
					if "-" in fileName: 
						cdNumber = "CD" + fileName[:1]  
						titleStartMarker = 5 
					newAlbumPath = os.path.join(cwd,albumDir,cdNumber) 
					if not os.path.exists(newAlbumPath):  
 						os.makedirs(newAlbumPath) 
					newFileName = artistDir + " - " + fileName[titleStartMarker:len(fileName)] 
					newFileName = newFileName.lower() 
					os.rename(fileName,newFileName) 
					newFilePath = os.path.join(newAlbumPath,newFileName) 
					print newFilePath 
					shutil.move(newFileName,newFilePath) 
		os.chdir(cwd) 
		shutil.rmtree(artistDir) 