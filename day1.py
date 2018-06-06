# Day 1 of Python course

num = 7

num_float = 7.0

l = [2,3,4,5,6]

item = 3
print(item == 3)

#note that when you aren't in the console you have to use the
#print function to get an output

myStr = "This is my string!"
print(myStr)
print(myStr[0],myStr[9],myStr[-1])
myStr = myStr + "biatch"
#An equivalent way to do this is myStr += "biatch"

print(myStr.startswith('this'))
print(myStr.startswith('This'))

myList = [1, 'Jim', 17.3, [1,2,3,]]
myList.append('Jack')

#to instantiate tuples use () instead of []
myTuple = ('Emergency','Mad Kat','System')
#unlike lists, tuples are immutable

#dictionaries, also known as libraries, associate key:value pairs
charstats = {'Moose':[16,14,17], 'Cassandra':[10,16,13]}
print(charstats['Cassandra'])
charstats['Alex'] = [12,18,16]
print(charstats)
#print the keys of a dictionary
print(charstats.keys())

character = "Lana"

if character == "Archer":
    print("Danger Zone!")
elif character == "Lana":
    print("Noooooope!")
else:
    print("Inapropes.")
    
numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for YIPE in numList:
    print(YIPE)
    if YIPE == 9:
        print(YIPE)

secList = [10,20,30,40,50]
for num in numList:
	for secNum in secList:
		print num, secList