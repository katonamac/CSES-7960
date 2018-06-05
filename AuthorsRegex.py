#Project Gutenberg - count the number of author entries, make dictionary

import re

def howManyAuthors(file):
    source = open(file, 'r')

    regex = r', by (\D+)'

    result = re.findall(regex, source, re.M)
    authorList = []

    for item in result:
        item.rstrip()
        if item not in authorList:
            authorList.append(item)

    print(len(authorList))

    source.close()

howManyAuthors('gutenmod1997.txt')

#The following function works OK - don't mess with it
def authorCounts(authorList):
    uniqueAuthorList = []
    authorDict = {}

    for author in authorList:
        if author not in uniqueAuthorList:
            uniqueAuthorList.append(author)
        
    for author in uniqueAuthorList:
        authorDict[author] = authorList.count(author)
    
    return(authorDict)