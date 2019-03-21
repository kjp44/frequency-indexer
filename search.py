import os
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


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


def getTokens(pageText):
    tokens = word_tokenize(pageText)
    return tokens


def getStopWords(language):
    stopWords = set(stopwords.words(language))
    return stopWords


def indexPage(tokens, stopWords, index, pageCounter, indexedTerms):
    for token in tokens:
        if token not in stopWords:
            if token not in index:
                index[token] = {pageCounter: 1}
                indexedTerms.append(token)
            elif pageCounter not in index[token]:
                index[token][pageCounter] = 1
            else:
                index[token][pageCounter] += 1
