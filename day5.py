#Opening and writing to files

fileName = open('practiceTextFile.txt', 'r')

print(fileName)

for line in fileName:
    print(line)

print(type(fileName))

fileName.close()

#Because it is an object of a specific type, we know that there are attributes
#and methods associated with that type

#We will be using dot notation, see below methods:

fileName.read()
#This one prints the whole file as one string.
fileName.readline()
#This one goes through the lines one at a time.
fileName.readlines()
#This one puts all the lines into a list.

#How can we find the number of sequences in a FASTA file?
fasta = open('shortFasta.fasta', 'r')
counter = 0
for line in fasta:
	if line.startswith('>'):
		counter +=1
print counter

fasta.close()

#Writing to a file
ids = open('identifiers.txt','w')
fasta = open('shortFasta.fasta', 'r')

for line in fasta:
    if line.startswith('>'):
        ids.write(str(line) + '\n')

fasta.close()
ids.close()

ids = open('identifiers.txt','r')
for line in ids:
    print(line)
ids.close()

#Now make it a function
def getIdentifiers(readinfile, writeoutfile):
    ids = open(writeoutfile, 'w')
    fasta = open(readinfile, 'r')

    for line in fasta:
        if line.startswith('>'):
            ids.write(str(line) + '\n')

    fasta.close()
    ids.close()
    
#Homework - go to Project Gutenberg, pull up the 1997 index, 
#and write all the Shakespeare books to a file called Shakespeare.txt
#Also, do Practice 3 from Opening, Reading, and Writing to Docs