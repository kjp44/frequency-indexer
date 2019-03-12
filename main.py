import search

search.changeDirectory('Pages')

fileNames = search.getFileNames()

pageContent = search.getPageContent(fileNames[0])