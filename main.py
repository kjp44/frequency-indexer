import search

search.changeDirectory('Pages')

fileNames = search.getFileNames()

pageContent = search.getPageContent(fileNames[0])

soup = search.getSoup(pageContent)

pageText = search.getPageText(soup)

tokens = search.getTokens(pageText)

for token in tokens:
	print(token)