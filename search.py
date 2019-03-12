import os

def changeDirectory(path):
    os.chdir(path)

def getFileNames():
	fileNames = os.listdir()
	return fileNames