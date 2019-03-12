import os
from bs4 import BeautifulSoup


def changeDirectory(path):
    os.chdir(path)

def getFileNames():
	fileNames = os.listdir()
	return fileNames

def getPageContent(fileName):
	f = open(fileName, 'r', encoding='utf-8', errors='ignore')
	return f.read()

def getSoup(pageContent):
	soup = BeautifulSoup(pageContent, 'html.parser')
	for script in soup(["script", "style"]):
		script.decompose()
	return soup


def getPageText(soup):
    pageText = soup.get_text()
    return pageText
