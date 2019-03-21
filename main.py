import search
import save

search.changeDirectory('Pages')

fileNames = search.getFileNames()

pageCounter = 0

index = {}

indexedTerms = []

stopWords = search.getStopWords('english')

for fileName in fileNames:

    pageCounter += 1

    pageContent = search.getPageContent(fileName)

    soup = search.getSoup(pageContent)

    pageText = search.getPageText(soup)

    tokens = search.getTokens(pageText)

    print('Indexing page #' + str(pageCounter) + ': ' + fileName)

    search.indexPage(tokens, stopWords, index, pageCounter, indexedTerms)


sortedIndex = save.sortIndex(index)

save.saveFile('Index', '.txt', str(sortedIndex))

indexedTermsToSave = save.arrayToSave(indexedTerms)

save.saveFile('IndexedTerms', '.txt', indexedTermsToSave)
