import re
import pandas as pd
# This script will read in and write out the course file

rawHtml = open('thefileinquestion.txt', 'r')

courses = re.findall(r'<th CLASS=\"ddtitle\" scope=\"colgroup\" ><a href=\".*\">(.*)</a>', rawHtml, re.M)

rawHtml.close()
# Not working yet, skip down

# This part works to split the course info up into list form
testList = ["Global Geography - 10462 - GEOG 1010 - 001",
           "Global Geography - 10464 - GEOG 1010 - 003",
           "Human Geography - 14225 - GEOG 2010 - 001",
           "Introduction to Geographic Information Systems - 16850 - GEOG 5833 - 001"]

# This function works OK, pass it the list of courses and it will split them
# into their components to populate the dataframe

def cleanCourses(courseList):
    readyList = []

    for i in courseList:
        readyList.append(i.split(" - "))
    return readyList

# This function also works fine, call the previous function in its arg

def createCourseFrame(readyList):
    testDataFrame = pd.DataFrame(readyList, columns = ["Course Title", "CRN", "Course Number", "Section"])
    return testDataFrame

# Leave this alone, it works to create the .csv file, do this at the end with the complete dataframe
# prettyTable = testDataFrame.to_csv('thisTakesArguments.csv', header = True, index = False)
