'''This is a project for generating clean tables of course information from the raw HTML
output by Auburn's Course Search tool.  It will take in the HTML as a text file and output a .csv file.
I want to use BeautifulSoup to parse the HTML and get the right pieces, pandas to get it into a data frame,
and then when it comes time to write the file I want to create a filename based on user input.'''

import re
import sys
import os
import pandas as pd


def getCourses(filename):
    rawHtml = open(filename, 'r')
    courses = re.findall(r'<th CLASS=\"ddtitle\" scope=\"colgroup\" ><a href=\".*\">(.*)</a>', rawHtml)
    rawHtml.close()
    return courses


# This function works OK, pass it the list of courses and it will split them
# into their components to populate the dataframe

def cleanCourses(courseList):
    readyList = []

    for i in courseList:
        readyList.append(i.split(" - "))
    return readyList


def createCourseFrame(readyList):
    testDataFrame = pd.DataFrame(readyList, columns = ["Course Title", "CRN", "Course Number", "Section"])
    return testDataFrame


def writefile():
    # do something
    pass

def getUserInput():
    # do something
    pass