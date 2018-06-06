#Pandas and Pylab

#You can plot using either Pylab or Matplotlib (matplotlib.org)

import pylab

l = []
for i in range(1,100):
    l.append((i**3)/2.0)
    
pylab.plot(l)
pylab.show()

grades = [30, 40, 20, 5, 5]
letters = ['A', 'B', 'C', 'D', 'F']

pylab.pie(grades, labels = letters)

pylab.title('My terrible class\'s horrible grades')

pylab.legend(letters)

#Plotly is a good resource

#Remember to create modular, reusable code whenever possible

import pandas

#now use the pandas read_csv function to read a csv file into memory.

dataFile = pandas.read_csv('csvFileDataExample.csv')

print(type(dataFile))

#what is the type of the centi object?

print(dataFile)

# what printed?  What does that tell you?

print(dataFile.columns)

for header in dataFile.columns:
    print(header)

clemson = dataFile[dataFile['location'] == 'clemson']
#This slices out all of the data where the location is Clemson

newDataFile = pandas.read_csv('yetAnotherTable.csv')

newDataFile.pivot_table(values='control', index=['cultivar', 'pylex', 'sprint'])

newDataFile.pivot_table(values='control', index=['cultivar', 'pylex', 'sprint']).plot(kind='barh')

for header in newDataFile.columns:
    print(header)