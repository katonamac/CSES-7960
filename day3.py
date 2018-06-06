# -*- coding: utf-8 -*-
#Design a sequenced program that takes a given sequence of numbers 
#and sums the odd ones only, inclusive of the end points

init = 555
final = 3001
total = 0

while init <= final:
    if init % 2 == 1:
        total = total + init
    init += 1

#Note: It's OK to have a "naked" IF statement
print(total)

#For bioinformatics problems, check out rosalind.info

def stringCounter(listObject):
	counter = 0
	for item in listObject:
	    if type(item) == str:
	        counter += 1
	return counter

L = ['bubbles', 1, 1.3, "cats", "farmers", 'Yucatan', 'Over 9000!', 'forest']

stringCounter(L)

#If you want your function returned as a variable you can use again,
#you have to bind it to another name

#Here's my initial exercise as a function

def totalOdds(init, final):
    total = 0
    while init <= final:
        if init % 2 == 1:
            total = total + init
        init += 1
    return(total)
    
print totalOdds(555, 9000)

#The scope of the variable remains within the function

#Counting words in a string

taleOfTwo = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'

def tallyThoseWords(string):
    wordTally = {}
    lowerstring = string.lower()
    stringList = lowerstring.split(" ")
    return stringList
    for word in stringList:
        if word in wordTally:
            continue
        else:
            wordTally[word] = [1]
    return wordTally
        