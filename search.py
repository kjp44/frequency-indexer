import os

def changeDirectory(path):
    os.chdir(path)

def getFileNames():
	fileNames = os.listdir()
	return fileNames

def getPageContent(fileName):
	f = open(fileName, 'r', encoding='utf-8', errors='ignore')
	return f.read()
