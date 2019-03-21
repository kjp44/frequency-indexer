import search
import collections

search.changeDirectory('Pages')

fileNames = search.getFileNames()

index = {}

count = 0

for fileName in fileNames:
	count += 1
	print('Indexing file: ' + fileName)

	pageContent = search.getPageContent(fileName)

	soup = search.getSoup(pageContent)

	pageText = search.getPageText(soup)

	tokens = search.getTokens(pageText)

	for token in tokens:
		if token in index:
			index[token] = index[token] + 1
		else:
			index[token] = 1

orderedIndex = collections.OrderedDict(sorted(index.items()))

for key in orderedIndex:
	print(key + ': ' + str(index[key]))